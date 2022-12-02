import json
from typing import Optional, Any
import requests


class Delivery:

    def __init__(self):
        self.base_url = "https://api.trackingmore.com"
        self.api_key = ""
        self.get_key()
        self.api_version = "v3"
        self.headers = {
            "Content-Type": "application/json",
            "Tracking-Api-Key": self.api_key
        }
        self.SLEEP_TIME = 60

    def get_key(self) -> None:
        with open("key.txt", "r") as f:
            self.api_key = f.read()
            f.close()

    def save_tracking_data(self) -> None:
        url = self.base_url + "/" + self.api_version + "/trackings/get"
        results = requests.get(url, headers=self.headers)
        with open("results.json", "w") as f:
            json.dump(results.json(), f)

    @staticmethod
    def get_tracking_data() -> dict:
        with open("results.json", "r") as f:
            return json.load(f)

    def delivery_status(self) -> Optional[list[Any]]:
        if not self.get_tracking_data()["code"] == 200:
            print(f"{self.get_tracking_data()['code']} -> {self.get_tracking_data()['message']}\n"
                  f"https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/{self.get_tracking_data()['code']}")
            return None
        delivery = []
        data = self.get_tracking_data()["data"][0]
        delivery.append(data["tracking_number"])
        delivery.append(data["delivery_status"])
        delivery.append(data["update_date"])
        delivery.append(data["title"])
        time = delivery[2].split("T")
        delivery[2] = time[0]
        return delivery

    def run(self) -> None:
        self.save_tracking_data()
