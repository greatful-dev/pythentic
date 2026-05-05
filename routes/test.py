from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agent.stock_evaluator import generate_pentagon_scores

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

@router.get("/test-1")
async def get_test_root():
    return {"message": "Test router 1"}

@router.get("/test-2")
async def get_test_root():
    return {"message": "Test router 2"}

@router.get("/generate-pentagon-scores")
def get_pentagon_scores():
    return generate_pentagon_scores()
