import React, { useState } from "react"
import Header from "../components/Header"
import ChatArea from "../components/ChatArea"
import InputArea from "../components/InputArea"
import { useEffect } from "react";


const Chat = () => {
    const [conversation, setConversation] = useState([]);
    useEffect(() => {
        const fetchConversation = async () => {
            try {
                const response = await fetch("http://localhost:8800/api/get-conversation");
                const data = await response.json();

                setConversation(data.messages || []);
            } catch (error) {
                console.error(error);
            }
        };
        fetchConversation();
    }, []);


    const handleSendMessage = async (message) => {
        if (!message.trim()) return;
        try {
            const response = await fetch("http://localhost:8800/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ query: message })
            });
            const data = await response.json();
            console.log(data.response);
            setConversation([...conversation, { id: 1, sender: "user", text: message }]);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="flex h-screen flex-col bg-background overflow-hidden px-28">
            <Header />
            <ChatArea conversation={conversation} />
            <InputArea onSendMessage={handleSendMessage} />
        </div>
    )
}

export default Chat