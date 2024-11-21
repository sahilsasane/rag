import React from 'react'

const ChatArea = ({ conversation }) => {
    return (
        <div className="flex-1 overflow-y-auto p-3 md:p-4">
            <div className="space-y-6 md:space-y-4">
                {conversation.map(([id, _, userType, message], index) => (
                    <div key={id || index} className="flex items-start gap-3 md:gap-4">
                        <div
                            className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-full ${userType === "bot" ? "bg-emerald-100" : "bg-purple-200"
                                }`}
                        >
                            {userType === "bot" ? (
                                <img
                                    src="/bot.svg"
                                    alt="AI Avatar"
                                    className=""
                                />
                            ) : (
                                <span className="text-sm font-medium text-purple-700">S</span>
                            )}
                        </div>
                        <div className="rounded-lg bg-muted px-4 py-2.5 md:py-2">
                            <p className="text-base md:text-sm">{message}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>

    );
};

export default ChatArea