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
