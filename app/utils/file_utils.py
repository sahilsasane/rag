import os
import shutil
from fastapi import UploadFile, HTTPException


def save_uploaded_file(file: UploadFile, upload_folder: str) -> str:
    """
    Save an uploaded file to the specified folder.

    Args:
        file (UploadFile): The uploaded file
        upload_folder (str): Destination folder for the file

    Returns:
        str: Full path to the saved file
    """
    # Ensure upload folder exists
    os.makedirs(upload_folder, exist_ok=True)

    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF.")

    # Generate full file path
    file_path = os.path.join(upload_folder, file.filename)

    # Save file
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")
