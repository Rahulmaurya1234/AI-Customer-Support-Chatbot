from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.concurrency import run_in_threadpool

from chatbot import get_response

app = FastAPI(
    title="AI Customer Support Bot",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
async def home():
    return {
        "status": "running",
        "project": "AI Customer Support Bot"
    }


@app.post("/chat")
async def chat(data: ChatRequest):

    reply = await run_in_threadpool(
        get_response,
        data.message
    )

    return {
        "reply": reply
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )