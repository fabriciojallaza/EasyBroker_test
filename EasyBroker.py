import requests


class EasyBrokerAPI:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "X-Authorization": access_token,
            "Content-Type": "application/json"
        }
        self.base_url = "https://api.stagingeb.com/v1/contact_requests"

    def get_properties(self):
        url = f"{self.base_url}"  # /properties
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            properties_raw = response.json()
            properties_raw = properties_raw["content"]

            keys_of_properties = properties_raw[0].keys()

            return properties_raw, keys_of_properties
        else:
            return []
