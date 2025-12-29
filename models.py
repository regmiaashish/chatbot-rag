from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class PDFDocument(Base):
    __tablename__ = "pdf_documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(LargeBinary)

