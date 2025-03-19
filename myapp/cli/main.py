import click
from quart import Blueprint

from myapp.models import *
from myapp.factory import db


bp = Blueprint("cli", "cli", cli_group=None)


@bp.cli.command("ping", with_appcontext=True)
def generate():
    click.echo("pong")
