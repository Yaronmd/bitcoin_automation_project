
from unittest.mock import patch
import pytest
from main import run_automation


@patch("main.time.sleep", return_value=None)
def test_run_automation_calls_sleep(mock_sleep):
    with patch("main.fetch_and_save"), \
         patch("main.clear_file", side_effect=KeyboardInterrupt), \
         patch("main.save_plot"), \
         patch("main.send_email"), \
         patch("main.logger"):

        with pytest.raises(KeyboardInterrupt):
            run_automation()

    # ✅ Validate sleep was called
    mock_sleep.assert_called_with(60)