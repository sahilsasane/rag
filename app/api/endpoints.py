from fastapi import APIRouter, File, UploadFile, Depends
from core.embeddings import EmbeddingsManager
from utils.file_utils import save_uploaded_file
from core.chatbot import ChatbotManager
from schema.requests import QueryRequest
from schema.db_models import MessageRepository, DATABASE_URL

router = APIRouter()
message_repo = MessageRepository(DATABASE_URL)

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
        qdrant_url="http://localhost:6333",
        collection_name="vector_db",
    )
    result = embeddings_manager.create_embeddings(file_path)

    return {
        "filename": file.filename,
        "message": "PDF uploaded successfully!",
        "embeddings": result,
    }

@router.post("/chat")
async def query_embeddings(request: QueryRequest):
    """
    Process a query and generate a response.

    Args:
        request (QueryRequest): User's query

    Returns:
        Dict with generated response
    """
    bot = ChatbotManager(
        model_name="BAAI/bge-small-en",
        device="cpu",
        encode_kwargs={"normalize_embeddings": True},
        llm_model="llama3.2:3b",
        llm_temperature=0.7,
        qdrant_url="http://localhost:6333",
        collection_name="vector_db",
    )
    response = bot.get_response(request.query)

    message_repo.add_message(
        conversation_id=1,
        sender="user",
        message=request.query
    )
    message_repo.add_message(
        conversation_id=1,
        sender="bot",
        message=response
    )

    return {"response": response}