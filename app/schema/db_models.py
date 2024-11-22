from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os
from typing import List, Optional

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, index=True)
    sender = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class MessageRepository:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def get_conversation_messages(self, conversation_id: int) -> List[Message]:
        """Get all messages for a specific conversation."""
        session = self.SessionLocal()
        try:
            messages = (
                session.query(Message)
                .filter(Message.conversation_id == conversation_id)
                .order_by(Message.timestamp)
                .all()
            )
            return messages
        finally:
            session.close()

    def add_message(self, conversation_id: int, sender: str, message: str) -> Message:
        """Add a new message to the conversation."""
        session = self.SessionLocal()
        try:
            db_message = Message(
                conversation_id=conversation_id,
                sender=sender,
                message=message
            )
            session.add(db_message)
            session.commit()
            session.refresh(db_message)
            return db_message
        finally:
            session.close()

    def get_message_by_id(self, message_id: int) -> Optional[Message]:
        """Get a specific message by its ID."""
        session = self.SessionLocal()
        try:
            return session.query(Message).filter(Message.id == message_id).first()
        finally:
            session.close()

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/RAG"