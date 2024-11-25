from fastapi import APIRouter, HTTPException
from app.utils.qa_processing import answer_question

router = APIRouter()

@router.post("/ask")
async def ask_question(pdf_path: str, question: str):
    try:
        answer = answer_question(pdf_path, question)
        return {"question": question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
