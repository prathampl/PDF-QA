from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import pdf_processing, file_storage
from datetime import datetime

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Uploads a PDF file, extracts text content, and saves metadata.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    # Save file to storage
    file_path = await file_storage.save_file(file)
    
    # Extract text from the PDF
    text_content = pdf_processing.extract_text(file_path)
    
    # Save metadata and content
    metadata = {
        "filename": file.filename,
        "upload_date": datetime.now().strftime("%Y-%m-%d"),
        "content_length": len(text_content),
    }
    
    # Log metadata and return the result
    print(f"Metadata: {metadata}")
    return {"message": "File uploaded successfully", "metadata": metadata}
