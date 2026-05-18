from fastapi import APIRouter, File, UploadFile
from typing import List
from fastapi import BackgroundTasks
from app.services.notification_service import send_email
from app.config import MAX_FILE_SIZE
from app.schemas import FileResponse
from app.services.file_service import save_file, get_all_files

router = APIRouter()

@router.get("/config-test")
def config_test():

    return {
        "max_file_size": MAX_FILE_SIZE
    }

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await save_file(file)

@router.post("/notify")
async def notify(
    email: str,
    background_tasks: BackgroundTasks
):

    background_tasks.add_task(send_email, email)

    return {
        "message": "Notification task started"
    }

@router.get("/files",response_model=List[FileResponse])
def get_files():
	return get_all_files()

