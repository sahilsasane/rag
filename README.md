# Real-Time Chat Application with WebSocket and AI Chatbot

This project is a real-time chat application that integrates a WebSocket server with an AI-powered chatbot. The chatbot processes user input and responds intelligently, while all messages are managed and displayed in real-time.

---

## **Project Directory Structure**
```
.
├── app         # Backend server with WebSocket and chatbot logic
├── client      # Frontend React application
```

---

## **Setup Instructions**

### **Backend (`app`)**

1. **Navigate to the `app` directory:**
   ```bash
   cd app
   ```

2. **Install dependencies:**
   Ensure you have Python 3.8 or later installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Qdrant (Vector Database):**
   Start a Qdrant container using Docker:
   ```bash
   docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
   ```

4. **Set Up PostgreSQL Database:**

   - Ensure PostgreSQL is installed and running.
   - Create a database named `RAG` by executing the following commands in the PostgreSQL CLI or any PostgreSQL GUI tool:
     ```sql
     CREATE DATABASE RAG;
     ```

   - Update the database connection settings in your backend's configuration file (e.g., `.env` or a settings module) to point to the `RAG` database.

---

### **Frontend (`client`)**

1. **Navigate to the `client` directory:**
   ```bash
   cd client
   ```

2. **Install dependencies:**
   Ensure you have Node.js and npm installed, then run:
   ```bash
   npm install
   ```

---

## **Running the Project**

### **Step 1: Start the Backend**

- From the `app` directory, run the backend server:
  ```bash
  uvicorn main:app --reload
  ```

### **Step 2: Start the Frontend**

- From the `client` directory, run the React development server:
  ```bash
  npm start
  ```

---

## **Features**

1. **Real-Time Communication**:
   - Bi-directional communication using WebSockets.
   - Broadcasts bot responses to all connected clients.

2. **AI-Powered Responses**:
   - Integrates a chatbot with an LLM model to generate intelligent responses.
   - Utilizes a vector database (Qdrant) for efficient query handling.

3. **Persistent Message Storage**:
   - User and bot messages are logged to a PostgreSQL database (`RAG`) for future retrieval.

4. **Dynamic Frontend**:
   - Modern React interface for seamless user interaction.

---

## **Tech Stack**

### **Backend**
- **FastAPI**: Framework for building the WebSocket server.
- **PostgreSQL**: Relational database for persistent message storage.
- **Qdrant**: Vector database for storing embeddings and improving chatbot responses.
- **Docker**: Containerized database for easy deployment.

### **Frontend**
- **React**: Frontend framework for building the user interface.
- **WebSocket API**: Enables real-time message handling.

---

## **Developer Notes**
- Ensure Docker is installed and running for Qdrant initialization.
- Configure the chatbot (`ChatbotManager`) and database connection settings as per your use case.
- Use `.env` files for storing sensitive configurations like API keys and database credentials.

---

## **License**
This project is licensed under the [MIT License](LICENSE).