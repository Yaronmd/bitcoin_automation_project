import os
import smtplib
from email.message import EmailMessage

from helper.logger_helper import logger


class EmailSender:
    """
    A utility class to send emails with file attachments using Gmail's SMTP server.

    """

    def __init__(self, sender_email, app_password, receiver_email):
        """
        Initialize the EmailSender with sender credentials and recipient address.

        Args:
            sender_email (str): Sender's Gmail address.
            app_password (str): App password for SMTP authentication.
            receiver_email (str): Receiver's email address.
        """
        self.sender_email = sender_email
        self.app_password = app_password
        self.receiver_email = receiver_email

    def send_email_with_attachment(self, subject, body, file_path):
        """
        Send an email with a file attachment.

        Args:
            subject (str): The subject of the email.
            body (str): The text content of the email.
            file_path (str): The path to the file to attach.
        """
        msg = EmailMessage()
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        try:
            with open(file_path, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(file_path)
                msg.add_attachment(
                    file_data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_name,
                )

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.sender_email, self.app_password)
                smtp.send_message(msg)

            logger.info(
                f"Email sent to {self.receiver_email} with attachment: {file_name}"
            )
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
