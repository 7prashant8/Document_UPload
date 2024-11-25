from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.pdf_processing import process_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")
    
    # Process and save PDF
    saved_path = process_pdf(file)
    return {"message": "PDF uploaded successfully", "path": saved_path}
