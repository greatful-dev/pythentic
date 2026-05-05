from fastapi import FastAPI
from mcp_native.main import mcp_app
from routes.test import router as test_router

app = FastAPI(
    lifespan=mcp_app.lifespan
)

@app.get("/hello")
async def root():
    return {"message": "Hello World!!"}

app.include_router(test_router, prefix="/test", tags=["test"])

app.mount("/", mcp_app)
