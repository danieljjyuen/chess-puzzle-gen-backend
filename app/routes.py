from fastapi import APIRouter
from app.services import get_next_puzzle

router = APIRouter()

@router.get("/puzzle/next")
async def next_puzzle():
    return await get_next_puzzle()