
import os
from unittest.mock import MagicMock, patch
from dotenv import load_dotenv
import pytest
from helper.email_utils import send_email


def test_valid_configuration():
 
    load_dotenv("config/.env")
    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_receiver = os.getenv("EMAIL_RECEIVER")
        
    missing = []
    if not email_sender:
        missing.append("EMAIL_SENDER")
    if not email_password:
        missing.append("EMAIL_PASSWORD")
    if not email_receiver:
        missing.append("EMAIL_RECEIVER")
    
    assert not missing, f"Missing environment variables: {', '.join(missing)}"
        
@patch("helper.email_utils.get_max_bitcoin")
@patch("helper.email_utils.EmailSender")
@patch("helper.email_utils.os.getenv")
@patch("helper.email_utils.load_dotenv")
def test_send_email_success(mock_load_dotenv, mock_getenv, mock_email_sender_class, mock_get_max_bitcoin):
    # Mock environment variables
    email_sender = "test@example.com"
    email_password = "password"
    email_recevier = "to@exmaple.com"
    body = "Max price: 12345 at 18/05/25 12:00:00"
    plot_file = "plot.png"
    
    
    mock_getenv.side_effect = lambda key: {
        "EMAIL_SENDER": email_sender,
        "EMAIL_PASSWORD":email_password,
        "EMAIL_RECEIVER": email_recevier
    }.get(key)

    # Mock get_max_bitcoin return
    
    mock_get_max_bitcoin.return_value = body

    # Mock EmailSender instance and method
    mock_email_sender = MagicMock()
    mock_email_sender_class.return_value = mock_email_sender

    send_email(json_path="data.json", plot_path=plot_file)

    mock_email_sender_class.assert_called_once_with(email_sender, email_password, email_recevier)

    # Assert send_email_with_attachment was called correctly
    mock_email_sender.send_email_with_attachment.assert_called_once_with(
        "Bitcoin automation",
        body=body,
        file_path=plot_file
    )
    

@patch("helper.email_utils.os.getenv")
@patch("helper.email_utils.load_dotenv")    
def test_invalid_email_configuration( mock_load_dotenv, mock_getenv):

    mock_getenv.return_value = None

    with pytest.raises(ValueError, match="Missing email configuration"):
        send_email(json_path="data.json", plot_path="plot.png")
        
