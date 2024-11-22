from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import endpoints
import uvicorn
import logging

logging.basicConfig(level=logging.DEBUG)

def create_app() -> FastAPI:
    app = FastAPI(
        title="PDF Query Chatbot with WebSocket",
        description="A FastAPI app with PDF query and real-time chat",
        version="0.1.0",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update to your frontend URL
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(endpoints.router, prefix="/api", tags=["PDF", "Embeddings", "Query"])
    app.add_websocket_route("/ws/chat", endpoints.websocket_endpoint)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app

if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="127.0.0.1", port=8800)
