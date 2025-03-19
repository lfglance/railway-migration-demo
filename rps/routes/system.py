from quart import Blueprint, jsonify

from rps.library.cache import cache
from rps.models import *

bp = Blueprint("system", "system")

@bp.route("/health")
async def index():
    print()
    return jsonify({
        "status": "ok",
        "version": "1",
        "sessions": len([k.decode() for k in cache.redis.keys('*')]),
        "matches": Match.query.filter().count(),
        "players": Player.query.filter().count()
    })
