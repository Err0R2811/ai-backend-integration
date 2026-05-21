from sqlalchemy.orm import Session
from app.models  import FileRecord

def create_file (db:Session,filename:str):
	new_file=FileRecord(filename=filename)


	db.add(new_file)

	db.commit()

	db.refresh(new_file)

	return new_file

def get_all_files (db:Session):
	files=db.query(FileRecord).all()
	return files
def get_file_by_id(
    db: Session,
    file_id: int
):

    file_record = db.query(FileRecord).filter(
        FileRecord.id == file_id
    ).first()

    return file_record
    
def delete_file_by_id(
    db: Session,
    file_id: int
):

    file_record = db.query(FileRecord).filter(
        FileRecord.id == file_id
    ).first()

    if file_record is None:
        return None

    db.delete(file_record)

    db.commit()

    return file_record
    
