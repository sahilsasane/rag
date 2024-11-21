import React, { useState } from "react";
import { FileText, Plus } from "lucide-react";

const Header = () => {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleUpload = async () => {
        if (!file) {
            console.error("No file selected");
            return;
        }
        setLoading(true);
        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("http://localhost:8800/api/upload-pdf", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            const data = await response.json();
            console.log("Upload successful:", data);
        } catch (error) {
            console.error("Upload failed:", error);
        } finally {
            setLoading(false);
        }

    };

    return (
        <header className="border-b">
            <div className="container flex h-14 md:h-16 items-center justify-between px-4">
                <div className="flex items-center gap-2">
                    <img
                        src="/logo.svg"
                        alt="AI Planet Logo"
                        className="h-20 w-20"
                    />
                </div>
                <div className="flex items-center gap-2 md:gap-4">
                    <div className="flex items-center gap-2">
                        <label
                            htmlFor="file-upload"
                            className="border border-black flex justify-center items-center rounded-md p-1 gap-2 cursor-pointer"
                        >
                            <Plus className="h-4 w-4" />
                            {file ? file.name : "Upload PDF"}
                        </label>
                        <input
                            id="file-upload"
                            type="file"
                            className="hidden"
                            accept=".pdf"
                            onChange={(e) => setFile(e.target.files[0])}
                        />
                    </div>
                    <button
                        onClick={handleUpload}
                        className={`border rounded-md p-1 ${loading ? "bg-gray-300 text-gray-500" : "border-blue-600 text-blue-600"
                            }`}
                        disabled={loading}
                    >
                        {loading ? "Uploading..." : "Upload"}
                    </button>
                </div>
            </div>
        </header>
    );
};

export default Header;
