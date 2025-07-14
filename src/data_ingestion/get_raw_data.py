import os

import requests
from dotenv import load_dotenv

from src.config.setup_logger import setup_logger
from src.storage_commons.mongodb_utils import (
    create_unique_index,
    get_mongo_client,
    insert_documents,
)

log = setup_logger()
log.info("Logger initialized successfully!")
load_dotenv()


class GetRawData:
    def __init__(self, source: str, base_url: str):
        self.source = source
        self.base_url = base_url
        self.client = get_mongo_client()
        self.collection = self.client["airline_data_system"][self.source]
        create_unique_index(self.collection, "airport_id")  # One-time setup

        log.info(f"Starting to get data from {self.source}.")
        log.info(f"URL {self.base_url.split('?')[0]}.")

    def fetch_all(self):
        offset = self.collection.count_documents({})
        limit = 100

        while True:
            log.info(f"Starting from register: {offset}.")
            response = requests.get(
                self.base_url, params={"offset": offset, "limit": limit}
            )
            data = response.json().get("data", [])

            if not data:
                break

            insert_documents(self.collection, data)

            if len(data) < limit:
                break

            offset += limit


if __name__ == "__main__":
    base_url = os.getenv("AVIATIONSTACK_API_AIRPORTS_URL")
    api_key = os.getenv("AVIATIONSTACK_API_KEY")

    if not base_url or not api_key:
        raise ValueError("Missing required environment variables.")

    url = base_url + api_key
    GetRawData("aviationstack", url).fetch_all()
