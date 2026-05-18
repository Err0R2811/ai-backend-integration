from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.middleware.logging import log_requests
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.middleware("http")(log_requests)
app.include_router(upload_router)

@app.get("/")
def read_root():
    return {"message": "API is running"}
