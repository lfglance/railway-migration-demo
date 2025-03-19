from quart import Blueprint, render_template


bp = Blueprint("main", "main")

@bp.route("/")
async def index():
    return await render_template("main/index.html")
