import React, { useEffect } from 'react'

const ChatArea = ({ conversation, loading }) => {
    // console.log(conversation);
    useEffect(() => {
        const chatArea = document.getElementById("chat-area");
        if (chatArea) {
            chatArea.scrollTo({
                top: chatArea.scrollHeight,
                behavior: "smooth"
            });
        }
    }, [conversation])
    return (
        <div className="flex-1 overflow-y-auto p-3 md:p-4" id='chat-area'>
            <div className="space-y-6 md:space-y-4">
                {conversation.map(({ id, message, sender }, index) => (
                    <div key={index} className="flex items-start gap-3 md:gap-4">
                        <div
                            className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-full ${sender === "bot" ? "bg-emerald-100" : "bg-purple-200"
                                }`}
                        >
                            {sender === "bot" ? (
                                <img
                                    src="/bot.svg"
                                    alt="AI Avatar"
                                    className=""
                                />
                            ) : (
                                <span className="text-sm font-medium text-purple-700">S</span>
                            )}
                        </div>
                        <div className="">
                            {loading && index == conversation.length - 1 ?
                                <div className="rounded-lg bg-muted px-4">
                                    <video
                                        src="/loading.webm"
                                        autoPlay
                                        loop
                                        muted
                                        className="h-8 w-12 p-0 m-0"
                                    /> </div> : <div className="rounded-lg bg-muted px-4 py-2.5 md:py-2"><p className="text-base md:text-sm">{message}</p></div>}
                        </div>
                    </div>
                ))}
            </div>
        </div>

    );
};

export default ChatArea