import React from 'react'
import { Button } from "../components/Button"
import { FileText, Plus } from 'lucide-react'

const Header = () => {
    return (
        <header className="border-b">
            <div className="container flex h-14 md:h-16 items-center justify-between px-4">
                <div className="flex items-center gap-2">
                    <img
                        src="/logo.svg"
                        alt="AI Planet Logo"
                        className="h-20 w-20 "
                    />
                </div>
                <div className="flex items-center gap-2 md:gap-4">
                    <Button variant="outline" size="icon" className="md:hidden">
                        <FileText className="h-4 w-4" />
                    </Button>
                    <div className="hidden md:flex">
                        <Button size="sm" className="gap-2 text-green-600">
                            <FileText className="h-4 w-4" />
                            demo.pdf
                        </Button>
                    </div>
                    <Button size="icon" className="md:hidden">
                        <Plus className="h-4 w-4" />
                    </Button>
                    <Button
                        size="sm"
                        className="border border-black hidden md:flex gap-2"
                        onClick={() => alert("Upload PDF")}
                    >
                        <Plus className="h-4 w-4" />
                        Upload PDF
                    </Button>
                </div>
            </div>
        </header>
    )
}

export default Header