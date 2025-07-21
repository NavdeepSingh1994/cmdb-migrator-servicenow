import requests
from dotenv import load_dotenv
import os

load_dotenv()

class ServiceNowAPI:
    def __init__(self):
        self.instance = os.getenv("SN_INSTANCE")
        self.user = os.getenv("SN_USER")
        self.password = os.getenv("SN_PASSWORD")
        self.base_url = f"https://{self.instance}/api/now/table/"

    def create_ci(self, table, data):
        response = requests.post(
            self.base_url + table,
            auth=(self.user, self.password),
            json=data
        )
        print(f"POST to {table}: {response.status_code}")
        return response.json()
