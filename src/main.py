import typer

from modules.cep.service import CepService
from infra.utils.tabulate import Tabulator

cli = typer.Typer()


@cli.command()
def cep(cep: str, api_cep_version: int = 1, tabulate: bool = False):
    result = CepService().execute(cep, api_cep_version)
    if tabulate:
        Tabulator("CEP").execute(result)
    else:
        print(f"{result}")


if __name__ == "__main__":
    cli()
