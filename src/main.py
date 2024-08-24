import typer

from modules.cep.service import CepService

cli = typer.Typer()


@cli.command()
def cep(cep: str):
    service = CepService()
    response = service.make_request_v1(cep)
    print(f"response: {response}")


if __name__ == "__main__":
    cli()
