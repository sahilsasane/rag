import React, { useState, useEffect, useRef } from "react";
import "./App.css";

const Test = () => {
    const [messages, setMessages] = useState([]); // Store chat messages
    const [input, setInput] = useState(""); // Input field value
    const socketRef = useRef(null); // WebSocket reference

    useEffect(() => {
        // Initialize WebSocket connection
        socketRef.current = new WebSocket("ws://127.0.0.1:8800/ws/chat");

        socketRef.current.onopen = () => {
            console.log("Connected to WebSocket server");
        };

        socketRef.current.onmessage = (event) => {
            const newMessage = event.data;
            setMessages((prev) => [...prev, newMessage]); // Add new message to state
        };

        socketRef.current.onclose = () => {
            console.log("Disconnected from WebSocket server");
        };

        return () => {
            // Clean up on component unmount
            if (socketRef.current) {
                socketRef.current.close();
            }
        };
    }, []);

    const sendMessage = () => {
        if (socketRef.current && input.trim() !== "") {
            socketRef.current.send(input);
            setMessages((prev) => [...prev, `You: ${input}`]); // Add user message
            setInput(""); // Clear input field
        }
    };

    return (
        <div className="App">
            <h1>Real-Time Chat</h1>
            <div className="chat-container">
                <div className="messages">
                    {messages.map((msg, index) => (
                        <div key={index} className="message">
                            {msg}
                        </div>
                    ))}
                </div>
                <div className="input-container">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        placeholder="Type a message..."
                    />
                    <button onClick={sendMessage}>Send</button>
                </div>
            </div>
        </div>
    );
};

export default Test;
