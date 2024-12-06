import React, { useEffect } from 'react'
import ReactMarkdown from 'react-markdown'

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
            {conversation.length === 0 ? (
                <div className="flex flex-col justify-center items-center h-full">
                    <img src="/emoji.png" alt="No conversation" className='h-48 w-48 transition-opacity ease-in duration-700 opacity-50 hover:opacity-25' />
                    <span className='p-5 bg-chatbg opacity-80 font-bold px-20 rounded-3xl'>Rag App</span>
                </div>
            ) :

                <div className="space-y-6 md:space-y-4">
                    {conversation.map(({ id, message, sender }, index) => (
                        <div key={index} className="flex items-start gap-3 md:gap-4">
                            <div
                                className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-full ${sender === "bot" ? "bg-emerald-100" : "bg-purple-200"
                                    }`}
                            >
                                {sender === "bot" ? (
                                    <img
                                        src="/emoji.png"
                                        alt="AI"
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
                                        />
                                    </div> :
                                    <div className="rounded-lg bg-muted px-4 py-2.5 md:py-2">
                                        <ReactMarkdown
                                            className="text-base md:text-sm"
                                            components={{
                                                a: ({ node, ...props }) => (
                                                    <a
                                                        {...props}
                                                        target="_blank"
                                                        rel="noopener noreferrer"
                                                        className="text-blue-600 hover:underline"
                                                    />
                                                ),
                                                code: ({ node, ...props }) => (
                                                    <code
                                                        {...props}
                                                        className="bg-gray-100 p-1 rounded text-sm"
                                                    />
                                                )
                                            }}
                                        >
                                            {message}
                                        </ReactMarkdown>
                                    </div>
                                }
                            </div>
                        </div>
                    ))}
                </div>
            }
        </div>

    );
};

export default ChatArea