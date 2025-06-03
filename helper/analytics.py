import pandas as pd

from helper.logger_helper import logger


def get_max_bitcoin(json_lines_path):

    try:

        df = pd.read_json(json_lines_path)
        if "price" not in df.columns or "timestamp" not in df.columns:
            logger.error("Missing 'price' or 'timestamp' columns.")
            raise ValueError("Missing 'price' or 'timestamp' columns.")

        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

        df = df.dropna(subset=["price", "timestamp"])

        max_row = df.loc[df["price"].idxmax()]
        formatted_time = max_row["timestamp"].strftime("%d/%m/%y %H:%M:%S")

        logger.info(f"Max BTC price: {max_row['price']} at {formatted_time}")
        return f"Max price: {float(max_row["price"])} at {formatted_time}"

    except Exception as e:
        error_message = "Failed to parse JSON or compute max price: {e}"
        logger.error(error_message)
        raise Exception(error_message)
    except Exception as e:
        error_message = f"Failed to catch json {e}"
        logger.error(error_message)
        raise Exception(error_message)
