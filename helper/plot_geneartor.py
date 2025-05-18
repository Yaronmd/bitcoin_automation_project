import pandas as pd
import matplotlib.pyplot as plt
from helper.logger_helper import logger
import matplotlib.dates as mdates

class PlotGenerator:
    def __init__(self, output_plot_file_path):
        self.output_plot_file_path = output_plot_file_path

    def generate_price_plot(self, json_path: str):
        try:

            df = pd.read_json(json_path, lines=True)

            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df["price"] = pd.to_numeric(df["price"])

            df = df.sort_values("timestamp")

            plt.figure(figsize=(10, 5))
            plt.plot(df["timestamp"], df["price"], marker="o", linestyle="-", color="blue")
            ax = plt.gca()
            ax.yaxis.get_major_formatter().set_useOffset(False)
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y %H:%M:%S"))
            ax.yaxis.get_major_formatter().set_useOffset(False)

            plt.title("BTC Price Over Time")
            plt.xlabel("Time")
            plt.ylabel("Price (USD)")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()

        
            plt.savefig(self.output_plot_file_path)
            plt.close()
            logger.info(f"Plot saved to {self.output_plot_file_path}")

        except Exception as e:
            error_message = f"Failed to generate plot: {e}"
            logger.error(error_message)
            raise Exception(error_message)


def save_plot(plot_file_path,data_path):
    plot_generator = PlotGenerator(plot_file_path)
    plot_generator.generate_price_plot(json_path=data_path)