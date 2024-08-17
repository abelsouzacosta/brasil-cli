from typing import Protocol


class IEndpointService(Protocol):
    def fetch_data_from_endpoint(self, endpoint: str): ...
