import React, { useState } from "react"
import { Button } from "../components/Button"
import { Input } from "../components/Input"
import { FileText, Plus } from 'lucide-react'
import Header from "../components/Header"
import ChatArea from "../components/ChatArea"
import InputArea from "../components/InputArea"

const Chat = () => {
    const [message, setMessage] = useState("")

    return (
        <div className="flex h-screen flex-col bg-background overflow-hidden px-28">
            <Header />
            <ChatArea />
            <InputArea />
        </div>
    )
}

export default Chat