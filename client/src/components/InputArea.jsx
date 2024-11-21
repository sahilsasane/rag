import React, { useState } from 'react'

const InputArea = ({ onSendMessage }) => {
    const [message, setMessage] = useState("")
    const sendMessage = () => {
        console.log(message);
        onSendMessage(message);
        setMessage("");
    }
    return (
        <div className="mb-5 p-3 md:p-4 mt-auto">
            <div className="container flex gap-2 max-w-full">
                <div className="flex items-center w-full rounded-md bg-background focus-within:ring-2 focus-within:ring-ring focus-within:ring-offset-2 shadow-md">
                    <input
                        type="text"
                        className="flex-grow h-14 px-3 py-2 text-sm bg-transparent focus:outline-none disabled:cursor-not-allowed disabled:opacity-50"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        placeholder='Type a message...'
                    />
                    <button
                        size="icon"
                        className="h-10 rounded-l-none pr-3"
                        onClick={(e) => sendMessage(e)}
                    >
                        <img src="/send.svg" alt="Send" className="h-4 w-4" />
                    </button>
                </div>
            </div>
        </div>
    )
}

export default InputArea