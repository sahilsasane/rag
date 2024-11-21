import React from 'react'


const ChatArea = () => {
    return (
        <div className="flex-1 overflow-y-auto p-3 md:p-4">
            <div className="space-y-6 md:space-y-4">
                {/* User Message */}
                <div className="flex items-start gap-3 md:gap-4">
                    <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-purple-200">
                        <span className="text-sm font-medium text-purple-700">S</span>
                    </div>
                    <div className="rounded-lg bg-muted px-4 py-2.5 md:py-2">
                        <p className="text-base md:text-sm">explain like im 5</p>
                    </div>
                </div>

                {/* AI Response */}
                <div className="flex items-start gap-3 md:gap-4">
                    <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-emerald-100">
                        <img
                            src="/bot.svg"
                            alt="AI Avatar"
                            className=""
                        />
                    </div>
                    <div className="rounded-lg bg-muted px-4 py-2.5 md:py-2">
                        <p className="text-base md:text-sm leading-relaxed">
                            Our own Large Language Model (LLM) is a type of AI that can learn from data. We have trained it on 7 billion
                            parameters which makes it better than other LLMs. We are featured on aiplanet.com and work with leading
                            enterprises to help them use AI securely and privately. We have a Generative AI Stack which helps reduce the
                            hallucinations in LLMs and allows enterprises to use AI in their applications.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ChatArea