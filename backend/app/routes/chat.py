from fastapi import APIRouter
from pydantic import BaseModel
from app.services.groq_chat import groq_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatReq(BaseModel):
    session_id: str
    message: str

chat_sessions = {}

@router.post("")
def chat(req: ChatReq):
    try:
        history = chat_sessions.get(req.session_id, [])
        history.append({"role": "user", "content": req.message})

        reply = groq_chat(history)

        history.append({"role": "assistant", "content": reply})
        chat_sessions[req.session_id] = history

        return {"reply": reply}

    except Exception as e:
        print("🔥 CHAT ERROR:", e)
        return {
            "reply": "AI service is temporarily unavailable. Please try again."
        }
