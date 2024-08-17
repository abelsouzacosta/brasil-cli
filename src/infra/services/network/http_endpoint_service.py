import requests


from domain.services.network.endpoint_service import IEndpointService


class HttpEndpointService(IEndpointService):
    def __init__(self, client=requests) -> None:
        self.client = client

    def fetch_data_from_endpoint(self, endpoint: str):
        response = self.client.get(endpoint)
        response.raise_for_status()
        return response.json()
