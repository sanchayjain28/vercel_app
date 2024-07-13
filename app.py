from main import router
import uvicorn
from fastapi import HTTPException, status, Depends, FastAPI
from fastapi.security import APIKeyHeader

app = FastAPI()

fast_api_demo_key = APIKeyHeader(name='Titan-API-key')



async def check_header(api_key: str = Depends(fast_api_demo_key)):
    if api_key != "1234sanchay":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key, Pass API key in header")
    return api_key


app.include_router(router, dependencies=[Depends(check_header)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
