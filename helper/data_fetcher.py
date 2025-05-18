import json
from datetime import datetime, timezone
import os
from api.api_client import APIClient
from helper.config_loader import ConfigLoader
from helper.logger_helper import logger

class DataFetcher:
    def __init__(self, client, endpoint: str, output_file: str):
        self.client = client
        self.endpoint = endpoint
        self.output_file = output_file

    def fetch_and_save(self):
        response = self.client.get(self.endpoint)
        if response.status == 200:
            data = response.json()
            price_data = data["data"]
            record = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "price": price_data["amount"]
            }
            self._save_to_file(record)
            logger.info(f"Fetched and saved at {record['timestamp']}")
        else:
            logger.warning(f"Failed to fetch: {response.status}")

    def _save_to_file(self, record):
        try:
            os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

            with open(self.output_file, "a") as f:
                json.dump(record, f)
                f.write("\n")
        except Exception as e:
            logger.error(f"Faild to write to file, expcetion: {e}")
    


def fetch_and_save(output_file:str):
    logger.info(f"Fetch data and save to {output_file}")
    config = ConfigLoader().get_api_config()
    base_url = config["base_url"]
    headers = config.get("default_headers", {}) 
    get_bitcoin_price_usd = config.get("get_bitcoin_price_usd")
    
    client = APIClient(base_url=base_url,default_headers=headers)
    
    data_featcher = DataFetcher(client=client,output_file=output_file,endpoint=get_bitcoin_price_usd)
    
    
    data_featcher.fetch_and_save()
    client.close()