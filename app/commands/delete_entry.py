from app.controllers.json import JsonController
from app.models.entry import Entry

import click


@click.command()
@click.argument('entry_id')
def delete(entry_id: int):
    json_controller = JsonController()
    did_delete = json_controller.delete_entry(entry_id)

    if not did_delete:
        return click.echo("There was a problem deleting your entry")
    
    return click.echo("Entry Deleted Successfully")