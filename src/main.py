from fastapi import FastAPI
from .auth.router import router as auth_router
from .history.router import router as history_router


app = FastAPI(title="Auth App")
app.include_router(auth_router)
app.include_router(history_router)

@app.get("/")
async def root():
    return {"Start": "App"}