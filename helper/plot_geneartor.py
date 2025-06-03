import os
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from helper.logger_helper import logger


class PlotGenerator:
    """
    Generating and saving a line plot of Bitcoin prices over time.
    """

    def __init__(self, output_plot_file_path):
        """
        Initialize the PlotGenerator.

        Args:
            output_plot_file_path (str): The path where the plot image will be saved.
        """
        self.output_plot_file_path = output_plot_file_path

    def generate_price_plot(self, json_path: str):
        """
        Generate and save a time-series line plot of BTC prices from a JSON lines file.

        Args:
            json_path (str): Path to the JSON lines file containing BTC price records.
        """
        try:
            if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
                raise ValueError("The JSON file is missing or empty.")
        
            df = pd.read_json(json_path)
            
            if df.empty:
                raise ValueError("DataFrame is empty after reading the JSON lines file.")

            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df["price"] = pd.to_numeric(df["price"])

            df = df.sort_values("timestamp")

            plt.figure(figsize=(10, 5))
            plt.plot(
                df["timestamp"], df["price"], marker="o", linestyle="-", color="blue"
            )
            ax = plt.gca()
            ax.yaxis.get_major_formatter().set_useOffset(False)
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%y %H:%M:%S"))
            ax.yaxis.get_major_formatter().set_useOffset(False)

            plt.title("Bitcoin Price Index (BPI) - Last Hour")
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


def save_plot(plot_file_path, data_path):
    logger.info("Save plot")
    plot_generator = PlotGenerator(plot_file_path)
    plot_generator.generate_price_plot(json_path=data_path)
