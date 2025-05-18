import json
import os
from dotenv import load_dotenv

load_dotenv()

class ConfigLoader:
    def __init__(self, path="api/api_config.json"):
        self.path = path
        try:
            with open(self.path, "r") as f:
                self.config = json.load(f)
        except Exception as e:
            print(f"Failed to load config file at {self.path}: {e}")
            self.config = {}

    def get_api_config(self):
        return self.config.get("api", {})
    
    
    