import os
from fastapi import UploadFile

UPLOAD_DIR = "data"

async def save_file(file: UploadFile) -> str:
    """
    Saves an uploaded file to the local filesystem.

    :param file: Uploaded file object.
    :return: Path to the saved file.
    """
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    return file_path
