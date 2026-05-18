import time
import uuid
from fastapi import Request
from app.core.logger import logger

async def log_requests(request: Request, call_next):

    start_time = time.time()
    request_id = str(uuid.uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    process_time = time.time() - start_time

    logger.info(
	f"ID={request_id}"
        f"{request.method} "
        f"{request.url.path} "
        f"- {response.status_code} "
        f"- {process_time:.4f}s"
    )

    return response
