import time

from app.core.logger import logger


def send_email(email: str):

    logger.info(f"Starting email send to {email}")

    time.sleep(5)

    logger.info(f"Finished email send to {email}")
