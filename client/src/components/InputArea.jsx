import React from 'react'
import { Input } from "../components/Input"
const InputArea = () => {
    const [message, setMessage] = React.useState("")
    return (
        <div className="mb-5 p-3 md:p-4 mt-auto">
            <div className="container flex gap-2 max-w-full">
                <Input
                    placeholder="Send a message..."
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    className="flex-1 text-base md:text-sm min-w-0"
                />
            </div>
        </div>
    )
}

export default InputArea