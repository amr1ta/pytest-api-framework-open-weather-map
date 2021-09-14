import os

import requests

API_KEY = os.getenv("OWM_API_KEY", "b1b15ee88fa797225412429c1c50c122a1")


class OpenWeatherMap_Client:
    def __init__(self, base_url="https://samples.openweathermap.org/data/2.5/"):
        self.base_url = base_url
        self.auth = f"appid={API_KEY}"
        self.session = requests.Session()

    def get_weather_data_by_city(self, city):
        url = f"{self.base_url}history/city?q={city}&{self.auth}"
        r = self.session.get(url)
        return r.status_code, r.json()
