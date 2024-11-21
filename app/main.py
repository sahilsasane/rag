from fastapi import FastAPI
from api import endpoints
import uvicorn

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured application instance
    """
    app = FastAPI(
        title="PDF Query Chatbot",
        description="A FastAPI application for PDF query and chat",
        version="0.1.0",
    )

    # Add routers
    app.include_router(
        endpoints.router, prefix="/v1", tags=["PDF", "Embeddings", "Query"]
    )

    # Health check endpoint
    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8800)



# from fastapi import FastAPI, File, UploadFile
# import shutil
# from embeddings import EmbeddingsManager
# from chatbot import ChatbotManager
# from pydantic import BaseModel
# import sqlite3
# import uvicorn


# class QueryRequest(BaseModel):
#     query: str


# app = FastAPI()


# @app.get("/health")
# def health():
#     return {"status": "ok"}


# @app.get("/")
# def read_root():
#     return {"message": ""}


# @app.get("/get-conversation")
# def get_conversation():
#     conn = sqlite3.connect("pdf_chat.db")
#     cursor = conn.cursor()
#     messages = cursor.execute(
#         "SELECT * FROM messages WHERE conversation_id = 1 ORDER BY timestamp;"
#     ).fetchall()
#     conn.close()
#     return {"messages": messages}


# @app.post("/upload-pdf")
# async def upload_pdf_and_get_embeddings(file: UploadFile = File(...)):
#     if file.content_type != "application/pdf":
#         return {"error": "File must be a PDF."}

#     file_path = f"./files/{file.filename}"

#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     embeddings_manager = EmbeddingsManager(
#         model_name="BAAI/bge-small-en",
#         device="cpu",
#         encode_kwargs={"normalize_embeddings": True},
#         qdrant_url="http://localhost:6333",
#         collection_name="vector_db",
#     )
#     result = embeddings_manager.create_embeddings(file_path)

#     return {
#         "filename": file.filename,
#         "message": "PDF uploaded successfully!,",
#         "embeddings": result,
#     }


# @app.post("/query")
# async def query_embeddings(request: QueryRequest):
#     bot = ChatbotManager(
#         model_name="BAAI/bge-small-en",
#         device="cpu",
#         encode_kwargs={"normalize_embeddings": True},
#         llm_model="llama3.2:3b",
#         llm_temperature=0.7,
#         qdrant_url="http://localhost:6333",
#         collection_name="vector_db",
#     )
#     response = bot.get_response(request.query)
#     conn = sqlite3.connect("pdf_chat.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO messages (conversation_id, sender, message) VALUES (?, ?, ?)",
#         (1, "user", request.query),
#     )

#     cursor.execute(
#         "INSERT INTO messages (conversation_id, sender, message) VALUES (?, ?, ?)",
#         (1, "bot", response),
#     )
#     conn.commit()
#     conn.close()
#     return {"response": response}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8800)