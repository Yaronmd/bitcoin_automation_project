import pytest

from helper.analytics import get_max_bitcoin


def test_not_exist_file():
    with pytest.raises(Exception):
        get_max_bitcoin("non_existent_file.json")


def test_valid_get_max_bitcoin(tmp_path):
    json_file = tmp_path / "dummy_data.json"
    json_file.write_text(
        '{"timestamp": "2025-05-18T10:00:00", "price": "64000"}\n'
        '{"timestamp": "2025-05-18T11:00:00", "price": "64500"}\n'
        '{"timestamp": "2025-05-18T12:00:00", "price": "63000"}\n'
    )

    result = get_max_bitcoin(str(json_file))

    assert isinstance(result, str)
    assert "Max price" in result
    assert "64500" in result
    assert "18/05/25 11:00:00" in result


def test_invalid_price_in_get_max_bitcoin(tmp_path):
    json_file = tmp_path / "dummy_data.json"
    json_file.write_text('{"timestamp": "2025-05-18T10:00:00", "price": "a"}\n')

    with pytest.raises(Exception, match="Failed to parse JSON or compute max price"):
        get_max_bitcoin(str(json_file))


def test_invalid_date_time_in_get_max_bitcoin(tmp_path):
    json_file = tmp_path / "dummy_data.json"
    json_file.write_text('{"timestamp": "a", "price": "100000"}\n')

    with pytest.raises(Exception, match="Failed to parse JSON or compute max price"):
        get_max_bitcoin(str(json_file))


def test_empty_file_get_max_bitcoin(tmp_path):
    json_file = tmp_path / "dummy_data.json"
    json_file.write_text("")

    with pytest.raises(Exception, match="Failed to parse JSON or compute max price"):
        get_max_bitcoin(str(json_file))
