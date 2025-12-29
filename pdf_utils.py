from pypdf import PdfReader

def extract_text_from_pdf(file_obj):
    reader = PdfReader(file_obj)          # file_obj is already a BytesIO
    return "".join(page.extract_text() or "" for page in reader.pages)