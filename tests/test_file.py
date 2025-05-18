from helper.file_utils import clear_file


def test_clear_file(tmp_path):
    json_file = tmp_path / "btc_data.json"
    clear_file(json_file)
    
    assert json_file.exists()
    assert json_file.stat().st_size == 0  