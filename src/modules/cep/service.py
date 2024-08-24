from typing import Optional

from domain.modules.cep.exceptions.invalid_api_version_exception import (
    InvalidApiVersionException,
)


from infra.services.network.http_endpoint_service import HttpEndpointService


class CepService:
    ENDPOINT_V1 = "https://brasilapi.com.br/api/cep/v1/"
    ENDPOINT_V2 = "https://brasilapi.com.br/api/cep/v2/"

    def __init__(self) -> None:
        self.client = HttpEndpointService()

    def make_request_v1(self, cep: str):
        response = self.client.fetch_data_from_endpoint(
            f"{CepService.ENDPOINT_V1}/{cep}"
        )
        return response

    def make_request_v2(self, cep: str):
        response = self.client.fetch_data_from_endpoint(
            f"{CepService.ENDPOINT_V2}/{cep}"
        )
        return response

    def execute(self, cep: str, version: Optional[int] = 1):
        if version is not None and version not in (1, 2):
            raise InvalidApiVersionException(
                f"Invalid Api Version: {version}, valid versions are: 1 or 2"
            )

        if version == 2:
            return self.make_request_v2(cep)

        return self.make_request_v1(cep)
