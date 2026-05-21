import os

from fastapi import HTTPException

from app.config import MAX_FILE_SIZE
from app.database import SessionLocal

from app.repositories.file_repository import (
    create_file,
    get_all_files as repo_get_all_files,
    get_file_by_id as repo_get_file_by_id,
    delete_file_by_id as repo_delete_file_by_id
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_file(file):

    if not file.filename.endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Only .txt files allowed"
        )

    content = await file.read()

    if len(content) == 0:
        raise HTTPException(
            status_code=400,
            detail="File is empty"
        )

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File too large"
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(content)

    db = SessionLocal()

    saved_file = create_file(
        db,
        file.filename
    )

    db.close()

    return {
        "id": saved_file.id,
        "filename": saved_file.filename
    }


def get_all_files():

    db = SessionLocal()

    files = repo_get_all_files(db)

    db.close()

    return files

def get_file_by_id(file_id:int):
    db=SessionLocal()
    file_record=repo_get_file_by_id(db,file_id)
    if file_record is None:
        db.close()
        raise HTTPException(
        status_code=404,
        detail="File not found"
        )
    db.close()
    return file_record
    
def delete_file_by_id(file_id: int):
    db=SessionLocal()
    deleted_file = repo_delete_file_by_id(
    db,
    file_id
    )
    if deleted_file is None:    
        db.close()
        raise HTTPException(
        status_code=404,
        detail="File not found"
        )
    db.close()
    return deleted_file
