from app.controllers.json import JsonController
from app.models.entry import Entry

import click


@click.command()
@click.argument('entry_id')
@click.option("--title", help="The updated title for the diary entry")
@click.option("--details", help="The updated details for the diary entry")
def edit(entry_id: int, title: str = None, details: str = None):
    if not title and not details:
        return click.echo("No Changes Made")
    
    json_controller = JsonController()

    found_entry = json_controller.get_entry(entry_id)

    if not found_entry:
        return click.echo(f"No Entry Found By ID: {entry_id}")
    
    updated_entry = Entry(
        entry_id = found_entry.entry_id,
        title = title if title else found_entry.title,
        details = details if details else found_entry.details,
        created_at = found_entry.created_at
    )

    did_save = json_controller.update_entry(updated_entry)

    if not did_save:
        return click.echo("There was a problem updating your entry")
    
    return click.echo("Entry Updated Successfully")