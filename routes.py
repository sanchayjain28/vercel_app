from fastapi import APIRouter


router = APIRouter()

@router.get('/')
async def root():
    return {"message": "Hello, World!"}
@router.get("/test")
async def test():
    return {"message": "Hello, World!"}
