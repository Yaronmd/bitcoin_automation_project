import os

from dotenv import load_dotenv

from helper.analytics import get_max_bitcoin
from helper.email_sender import EmailSender
from helper.logger_helper import logger


def send_email(json_path: str, plot_path: str):
    load_dotenv("config/.env")
    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_receiver = os.getenv("EMAIL_RECEIVER")

    if not email_sender or not email_password or not email_receiver:
        error_message = "Missing email configuration. Please check your .env file."
        logger.error(error_message)
        raise ValueError(error_message)

    email_password = email_password.replace(" ", "")
    email_sender = EmailSender(email_sender, email_password, email_receiver)

    email_sender.send_email_with_attachment(
        "Bitcoin automation", body=get_max_bitcoin(json_path), file_path=plot_path
    )
