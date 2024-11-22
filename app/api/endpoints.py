from fastapi import APIRouter, File, UploadFile, Depends, WebSocket, WebSocketDisconnect
from typing import List
from core.embeddings import EmbeddingsManager
from utils.file_utils import save_uploaded_file
from core.chatbot import ChatbotManager
from schema.requests import QueryRequest
from schema.db_models import MessageRepository
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
message_repo = MessageRepository(os.getenv("DATABASE_URL"))

@router.get("/get-conversation")
def get_conversation():
    messages = message_repo.get_conversation_messages(conversation_id=1)
    return {"messages": messages}

@router.post("/upload-pdf")
async def upload_pdf_and_get_embeddings(file: UploadFile = File(...)):
    """
    Upload a PDF file and generate embeddings.

    Args:
        file (UploadFile): PDF file to upload and process

    Returns:
        Dict with upload and embedding details
    """
    file_path = save_uploaded_file(file, "./files")

    embeddings_manager = EmbeddingsManager(
        model_name="BAAI/bge-small-en",
        device="cpu",
        encode_kwargs={"normalize_embeddings": True},
        qdrant_url=os.getenv("QDRANT_URL"),
        collection_name="vector_db",
    )
    result = embeddings_manager.create_embeddings(file_path)

    return {
        "filename": file.filename,
        "message": "PDF uploaded successfully!",
        "embeddings": result,
    }

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            bot = ChatbotManager(
                model_name="BAAI/bge-small-en",
                device="cpu",
                encode_kwargs={"normalize_embeddings": True},
                llm_model="llama3.2:3b",
                llm_temperature=0.7,
                qdrant_url="http://localhost:6333",
                collection_name="vector_db",
            )
            response = bot.get_response(data)
            message_repo.add_message(
                conversation_id=1,
                sender="user",
                message=data
            )
            message_repo.add_message(
                conversation_id=1,
                sender="bot",
                message=response
            )
            await manager.broadcast(f"{response}")
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client disconnected.")