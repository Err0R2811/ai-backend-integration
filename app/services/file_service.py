import os

from fastapi import HTTPException
from app. config import MAX_FILE_SIZE
from app.database import SessionLocal
from app.models import FileRecord

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

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(content)

    db = SessionLocal()

    file_record = FileRecord(filename=file.filename)

    db.add(file_record)
    db.commit()
    db.refresh(file_record)

    db.close()

    return {"id": file_record.id, "filename": file_record.filename}

def get_all_files():
	db = SessionLocal()
	
	files=db.query(FileRecord).all()

	db.close()
	
	return files
