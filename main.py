import asyncio
import json
from datetime import datetime
import requests


class Delivery:

    def __init__(self):
        self.base_url = "https://api.trackingmore.com"
        self.api_key = ""
        self.api_version = "v3"
        self.headers = {
            "Content-Type": "application/json",
            "Tracking-Api-Key": self.api_key
        }

    def save_tracking_data(self) -> None:
        url = self.base_url + "/" + self.api_version + "/trackings/get"
        results = requests.get(url, headers=self.headers)
        with open("results.json", "w") as f:
            json.dump(results.json(), f)

    @staticmethod
    def get_tracking_data() -> dict:
        with open("results.json", "r") as f:
            return json.load(f)

    def delivery_status(self) -> list:
        delivery = []
        if not self.get_tracking_data()["code"] == 200:
            return [self.get_tracking_data()["code"], self.get_tracking_data()["message"]]
        for key in self.get_tracking_data().keys():
            if key == "data":
                data = self.get_tracking_data()[key][0]
                for item in data.keys():
                    if len(delivery) == 3:
                        break
                    if item == "tracking_number":
                        delivery.append(data[item])
                    if item == "delivery_status":
                        delivery.append(data[item])
                    if item == "update_date":
                        delivery.append(data[item])
        time = delivery[2].split("T")
        delivery[2] = time[0]
        return delivery

    async def main(self) -> None:
        while True:
            self.save_tracking_data()
            data = self.delivery_status()
            print(
                f"Time – {datetime.now().strftime('%I:%M:%S %p')}"
                f"\nTracking Number: {data[0]}"
                f"\nDelivery Status: {data[1].upper()}"
                f"\nLast Update: {data[2]}"
            )
            print()
            await asyncio.sleep(60)


if __name__ == '__main__':
    delivery = Delivery()
    asyncio.run(delivery.main())
