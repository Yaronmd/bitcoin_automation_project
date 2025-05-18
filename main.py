from datetime import datetime, timedelta, timezone
import os
import time
from dotenv import load_dotenv
from helper.data_fetcher import  fetch_and_save
from helper.email_utils import send_email
from helper.file_utils import clear_file
from helper.logger_helper import logger
from helper.plot_geneartor import save_plot


def run_automation():
    logger.info("Bitcoin automation started")
    
    result_dir = "result"
    json_file = "data.json"
    plot_file = "btc_price_plot.png"
    
    os.makedirs(result_dir, exist_ok=True)
    json_output_path = os.path.join(result_dir, json_file)
    plot_output_path = os.path.join(result_dir,plot_file)

    last_email_sent = datetime.now(timezone.utc)
    one_hour = timedelta(hours=1)
    
    clear_file(json_output_path)
    try:
        while True:
            fetch_and_save(json_output_path)

            # Check if one hour has passed
            if datetime.now(timezone.utc) - last_email_sent >= one_hour:
                save_plot(plot_file_path=plot_output_path,data_path=json_output_path)
                send_email(json_path=json_output_path,plot_path=plot_output_path)
                clear_file(json_output_path)
                last_email_sent = datetime.now(timezone.utc)

            time.sleep(60)  
    except KeyboardInterrupt:
        logger.info("Stopped by user.")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
                
if __name__ == "__main__":
    run_automation()
    
    
    