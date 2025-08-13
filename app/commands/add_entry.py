from app.controllers.json import JsonController
from app.models.entry import EntryCreate

from datetime import datetime

import click


@click.command()
@click.option("--title", required=True, help="The title of the diary entry")
@click.option("--details", required=True, help="The details of the diary entry")
def add(title: str, details: str):
    json_controller = JsonController()

    all_entries = json_controller.get_entries()

    new_entry = EntryCreate(
        entry_id = len(all_entries) + 1,
        title = title,
        details = details,
        created_at = str(datetime.now())
    )

    did_save = json_controller.save_entry(new_entry)

    if not did_save:
        return click.echo("There was a problem saving your entry")

    return click.echo("Entry Saved Successfully")