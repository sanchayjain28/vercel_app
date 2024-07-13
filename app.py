from routes import router
import uvicorn
from fastapi import HTTPException, status, Depends, FastAPI
from fastapi.security import APIKeyHeader
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


app = FastAPI()

fast_api_demo_key = APIKeyHeader(name='fast_api_demo_key')

auth_key = os.getenv('fast_api_demo_key')

async def check_header(api_key: str = Depends(fast_api_demo_key)):
    if api_key != auth_key:
        print(api_key,' is not a valid API key',auth_key)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid API key, Pass API key in header{auth_key}, {api_key}")
    return api_key


app.include_router(router, dependencies=[Depends(check_header)])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
