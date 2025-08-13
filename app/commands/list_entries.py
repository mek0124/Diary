from app.controllers.json import JsonController

import click


@click.command()
@click.option("--entry_id", help="The entry id of the entry to display")
def list(entry_id: int = None):
    json_controller = JsonController()

    if entry_id:
        entry = json_controller.get_entry(entry_id)

        if not entry:
            return click.echo(f"No Entry Matching ID {entry_id} Exists")

        click.echo("------ All Entries ------")
        click.echo(f"ID: {entry.entry_id}")
        click.echo(f"Created At: {entry.created_at}")
        click.echo(f"Title: {entry.title}")
        return click.echo(f"Details: {entry.details}")
    
    all_entries = json_controller.get_entries()

    if not all_entries:
        return click.echo("No Entries Exist")
    
    click.echo("------ All Entries ------")

    for entry in all_entries:
        click.echo(f"ID: {entry.entry_id}")
        click.echo(f"Created At: {entry.created_at}")
        click.echo(f"Title: {entry.title}")
        click.echo(f"Details: {entry.details}")
        click.echo("-"*30)