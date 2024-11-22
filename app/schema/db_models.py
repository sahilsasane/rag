from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os
from dotenv import load_dotenv
from typing import List, Optional

load_dotenv()
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
        try:
            self.engine = create_engine(db_url)
            
            # Check if tables exist, create if not
            try:
                # Attempt to query a table to check if it exists
                with self.engine.connect() as connection:
                    connection.execute("SELECT 1 FROM messages LIMIT 1")
            except exc.SQLAlchemyError:
                # If table doesn't exist, create all tables
                Base.metadata.create_all(self.engine)
                print("Tables created successfully")

            self.SessionLocal = sessionmaker(bind=self.engine)
        except Exception as e:
            print(f"Error initializing database: {e}")
            raise

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
        except exc.SQLAlchemyError as e:
            print(f"Database error: {e}")
            return []
        finally:
            session.close()

    def add_message(self, conversation_id: int, sender: str, message: str) -> Optional[Message]:
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
        except exc.SQLAlchemyError as e:
            session.rollback()
            print(f"Error adding message: {e}")
            return None
        finally:
            session.close()

    def get_message_by_id(self, message_id: int) -> Optional[Message]:
        """Get a specific message by its ID."""
        session = self.SessionLocal()
        try:
            return session.query(Message).filter(Message.id == message_id).first()
        except exc.SQLAlchemyError as e:
            print(f"Database error: {e}")
            return None
        finally:
            session.close()

DATABASE_URL = os.getenv("DATABASE_URL")
repository = MessageRepository(DATABASE_URL)