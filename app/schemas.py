from pydantic import BaseModel

class FileResponse(BaseModel):
	id: int
	filename:str

class ErrorResponse(BaseModel):
	error:str

