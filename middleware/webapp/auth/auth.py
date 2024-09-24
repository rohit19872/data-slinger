import os
import requests


class Auth(object):
    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")

    def login(self):
        url = 'https://api.eka.care/connect-auth/v1/account/login'
        data = {
            "api_key": self.api_key,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise Exception("Failed to login")

        resp = response.json()
        access_token = resp.get("access_token")
        if not access_token:
            raise Exception("Failed to login")

        return access_token