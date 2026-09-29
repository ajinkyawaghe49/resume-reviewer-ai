from fastapi import FastAPI, UploadFile, File, HTTPException

from app.parser import extract_text_from_pdf
from app.ai_reviewer import review_resume


app = FastAPI()

MAX_FILE_SIZE = 5 * 1024 * 1024


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "resume-reviewer-ai"
    }


@app.get("/")
def home():
    return {
        "message": "Welcome to Resume Reviewer AI"
    }


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    # 1. Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # 2. Read file
    contents = await file.read()

    # 3. Validate empty file
    if not contents:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty"
        )

    # 4. Validate file size
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File size must be less than 5 MB"
        )

    # 5. Extract text
    try:
        resume_text = extract_text_from_pdf(contents)

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read the PDF file"
        )

    # 6. Validate extracted text
    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="No readable text found in the PDF"
        )

    # 7. AI review
    try:
        review = review_resume(resume_text)

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI review service is currently unavailable"
        )

    # 8. Return response
    return {
        "filename": file.filename,
        "review": review.model_dump()
    }