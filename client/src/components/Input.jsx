import * as React from "react"
import { Button } from "../components/Button"
import { cn } from "../lib/utils"

const Input = React.forwardRef(
    ({ className, type, ...props }, ref) => {
        return (
            <div className="flex items-center w-full rounded-md bg-background focus-within:ring-2 focus-within:ring-ring focus-within:ring-offset-2 shadow-md">
                <input
                    type={type}
                    className={cn(
                        "flex-grow h-14 px-3 py-2 text-sm bg-transparent focus:outline-none disabled:cursor-not-allowed disabled:opacity-50",
                        className
                    )}
                    ref={ref}
                    {...props}
                />
                <Button
                    size="icon"
                    className="h-10 rounded-l-none"
                    onClick={() => alert("Send Message")}
                >
                    <img src="/send.svg" alt="Send" className="h-4 w-4" />
                </Button>
            </div>
        )
    }
)
Input.displayName = "Input"

export { Input }