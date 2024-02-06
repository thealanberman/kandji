"""Kandji API Client"""

import requests


class API:

    def __init__(self, api_key, base_url="https://api.kandji.com", timeout=10):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.timeout = timeout

    def get(self, endpoint):
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            timeout=self.timeout,
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def post(self, endpoint, data):
        response = requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            timeout=self.timeout,
            json=data,
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def delete(self, endpoint):
        response = requests.delete(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            timeout=self.timeout,
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def patch(self, endpoint, data):
        response = requests.patch(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            timeout=self.timeout,
            json=data,
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def list_blueprints(self):
        return self.get(endpoint="/v1/blueprints")
