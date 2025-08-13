from app.commands.add_entry import add
from app.commands.edit_entry import edit
from app.commands.delete_entry import delete
from app.commands.list_entries import list

import click


@click.group()
def cli():
    pass


cli.add_command(add)
cli.add_command(edit)
cli.add_command(delete)
cli.add_command(list)


if __name__ == '__main__':
    cli()