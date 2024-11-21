from fastapi import APIRouter, File, UploadFile, Depends
from core.embeddings import EmbeddingsManager
from utils.file_utils import save_uploaded_file
from core.chatbot import ChatbotManager
from schema.requests import QueryRequest
import psycopg2

router = APIRouter()


@router.get("/get-conversation")
def get_conversation():
    conn = psycopg2.connect(
        dbname="RAG", user="postgres", password="admin", host="localhost", port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM messages WHERE conversation_id = %s ORDER BY timestamp;", (1,)
    )
    messages = cursor.fetchall()
    conn.close()
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
    # Save the uploaded file
    file_path = save_uploaded_file(file, "./files")

    # Create embeddings
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
    # Initialize managers
    bot = ChatbotManager(
        model_name="BAAI/bge-small-en",
        device="cpu",
        encode_kwargs={"normalize_embeddings": True},
        llm_model="llama3.2:3b",
        llm_temperature=0.7,
        qdrant_url="http://localhost:6333",
        collection_name="vector_db",
    )
    # Get response
    response = bot.get_response(request.query)

    conn = psycopg2.connect(
        dbname="RAG", user="postgres", password="admin", host="localhost", port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (conversation_id, sender, message) VALUES (%s, %s, %s)",
        (1, "user", request.query),
    )

    cursor.execute(
        "INSERT INTO messages (conversation_id, sender, message) VALUES (%s, %s, %s)",
        (1, "bot", response),
    )
    conn.commit()
    conn.close()
    return {"response": response}
