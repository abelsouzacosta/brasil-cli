import typer

from modules.cep.service import CepService

cli = typer.Typer()


@cli.command()
def cep(cep: str, api_cep_version: int = 1):
    result = CepService().execute(cep, api_cep_version)
    print(f"{result}")


if __name__ == "__main__":
    cli()
