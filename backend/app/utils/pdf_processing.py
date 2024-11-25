import os
from PyPDF2 import PdfReader

UPLOAD_DIR = "uploaded_pdfs"

def process_pdf(file):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path
