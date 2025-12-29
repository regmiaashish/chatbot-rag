from sqlalchemy.orm import Session
from models import PDFDocument, PDFChunk

def save_pdf(db: Session, filename: str, content: bytes):
    pdf = PDFDocument(filename=filename, content=content)
    db.add(pdf)
    db.commit()
    db.refresh(pdf)
    return pdf

def save_chunks(db: Session, pdf_id: int, chunks: list[str]):
    for chunk in chunks:
        db.add(PDFChunk(pdf_id=pdf_id, text=chunk))
    db.commit()

def get_chunks(db: Session, pdf_id: int):
    return [c.text for c in db.query(PDFChunk).filter_by(pdf_id=pdf_id).all()]
