from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

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
