from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import os, io, google.generativeai as genai
from database import engine, SessionLocal
from models import Base, PDFDocument
from pdf_utils import extract_text_from_pdf
from rag import GeminiRAG

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not set in .env")
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI(title="PDF RAG Chatbot")
app.mount("/static", StaticFiles(directory="static"), name="static")

rag: GeminiRAG | None = None

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

class ChatRequest(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
def ui():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/upload-pdf")
async def upload(file: UploadFile = File(...)):
    global rag
    if not file.filename.endswith(".pdf"):
        raise HTTPException(400, "Only PDF allowed")
    text = extract_text_from_pdf(io.BytesIO(await file.read()))
    if not text.strip():
        raise HTTPException(400, "Empty PDF")

    db = SessionLocal()
    pdf = PDFDocument(filename=file.filename)
    db.add(pdf); db.commit(); db.refresh(pdf); db.close()

    rag = GeminiRAG(text)          # defaults used
    return {"message": "PDF indexed", "pdf_id": pdf.id}

@app.post("/chat")
def chat(req: ChatRequest):
    if rag is None:
        raise HTTPException(400, "Upload a PDF first")
    return {"answer": rag.ask(req.query)}