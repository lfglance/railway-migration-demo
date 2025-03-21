from time import sleep

import click
from quart import Blueprint


bp = Blueprint("cli", "cli", cli_group=None)


@bp.cli.command("ping", with_appcontext=True)
def generate():
    while True:
        click.echo("pong")
        sleep(10)