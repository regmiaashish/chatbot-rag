from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, Text
from database import Base

class PDFDocument(Base):
    __tablename__ = "pdf_documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(LargeBinary)

class PDFChunk(Base):
    __tablename__ = "pdf_chunks"

    id = Column(Integer, primary_key=True)
    pdf_id = Column(Integer, ForeignKey("pdf_documents.id"))
    text = Column(Text)
