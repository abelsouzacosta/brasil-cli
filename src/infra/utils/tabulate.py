from rich.console import Console
from rich.table import Table


class Tabulator:
    def __init__(self, operation: str) -> None:
        self.table = Table(title=operation)
        self.console = Console()

    def draw_table(self, json_data):
        for key in json_data.keys():
            self.table.add_column(str(key))

    def insert_elements(self, json_data):
        data_keys = json_data.values()
        self.table.add_row(*data_keys)

    def execute(self, json):
        self.draw_table(json)
        self.insert_elements(json)
        self.console.print(self.table)
