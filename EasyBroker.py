import requests


class EasyBrokerAPI:
    def __init__(self, access_token):
        """
        Constructor de la clase EasyBrokerAPI

        Parameters:
        access_token (str): token de acceso a la API

        Attributes:
        access_token (str): token de acceso a la API
        headers (dict): encabezados HTTP que se usarán en cada solicitud a la API
        base_url (str): URL base de la API EasyBroker
        """
        self.access_token = access_token
        self.headers = {
            "X-Authorization": access_token,
            "Content-Type": "application/json"
        }
        self.base_url = "https://api.stagingeb.com/v1/contact_requests"

    def get_properties(self):
        """
        Método que obtiene todas las propiedades de la cuenta de EasyBroker

        Returns:
        tuple: Una tupla de dos elementos, la lista de propiedades y las claves de las propiedades
        Si no hay propiedades, se devuelve una lista vacía
        """
        url = f"{self.base_url}"  # /properties
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            properties_raw = response.json()
            properties_raw = properties_raw["content"]

            keys_of_properties = properties_raw[0].keys()

            return properties_raw, keys_of_properties
        else:
            return [], []