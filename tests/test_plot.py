import pytest
from helper.plot_geneartor import PlotGenerator


def test_generate_price_plot_creates_file(tmp_path):
    json_file = tmp_path / "btc_data.json"
    json_file.write_text(
        '{"timestamp": "2025-05-18T10:00:00", "price": "64000"}\n'
        '{"timestamp": "2025-05-18T11:00:00", "price": "64500"}\n'
        '{"timestamp": "2025-05-18T12:00:00", "price": "63000"}\n'
    )

    plot_file = tmp_path / "btc_plot.png"

    plotter = PlotGenerator(output_plot_file_path=str(plot_file))
    plotter.generate_price_plot(json_path=str(json_file))

    assert plot_file.exists()
    assert plot_file.stat().st_size > 0 
    
    
def test_generate_price_plot_creation_failed(tmp_path):

    json_file = tmp_path / "btc_data.json"
    json_file.write_text(
        '{ "price": "a"}\n'
    )

    plot_file = tmp_path / "btc_plot.png"

    plotter = PlotGenerator(output_plot_file_path=str(plot_file))

    with pytest.raises(Exception,match="Failed to generate plot:"):
        plotter.generate_price_plot(json_path=str(json_file))
        assert not plot_file.exists()
     