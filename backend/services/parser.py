import pdfplumber
import docx
from utils.file_handler import save_temp_file

def extract_text(file):
    path = save_temp_file(file)

    if file.filename.endswith(".pdf"):
        return extract_pdf(path)
    elif file.filename.endswith(".docx"):
        return extract_docx(path)
    else:
        raise ValueError("Unsupported file format")

def extract_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])
