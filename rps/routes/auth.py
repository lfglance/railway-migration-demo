from secrets import token_urlsafe

from quart import Blueprint, jsonify, request

from rps.factory import db
from rps.library.cache import cache
from rps.models import Player


bp = Blueprint("auth", "auth")

@bp.route("/register", methods=["POST"])
async def register():
    data = await request.get_json()
    player = Player(name=data["name"])
    db.session.add(player)
    db.session.commit()
    return jsonify({
        "id": player.id,
        "name": player.name
    }), 201

@bp.route("/authenticate", methods=["POST"])
async def authenticate():
    data = await request.get_json()
    player = Player.query.filter(Player.name == data["name"]).first()
    token = token_urlsafe(24)
    cache.set_data(f"session-{player.id}", 30, token)
    return jsonify({
        "token": token
    }), 201
