from helper.plot_geneartor import PlotGenerator


def test_generate_price_plot_creates_file(tmp_path):
    # dummy input JSON file
    json_file = tmp_path / "btc_data.json"
    json_file.write_text(
        '{"timestamp": "2025-05-18T10:00:00", "price": "64000"}\n'
        '{"timestamp": "2025-05-18T11:00:00", "price": "64500"}\n'
        '{"timestamp": "2025-05-18T12:00:00", "price": "63000"}\n'
    )

    plot_file = tmp_path / "btc_plot.png"

    # generate the plot
    plotter = PlotGenerator(output_plot_file_path=str(plot_file))
    plotter.generate_price_plot(json_path=str(json_file))

    # Assert: plot file was created and not empty
    assert plot_file.exists()
    assert plot_file.stat().st_size > 0  