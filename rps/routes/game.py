from quart import Blueprint, jsonify, request

from rps.factory import db
from rps.models import Match, MatchResult, Player

bp = Blueprint("game", "game")

@bp.route("/list")
async def list():
    results = MatchResult.query.filter()
    return jsonify({
        "matches": [
            {
                "id": i.id,
                "match": i.match_id,
                "winner": i.winner.name,
                "loser": i.loser.name,
                "winner_move": i.winner_move,
                "loser_move": i.loser_move
            } for i in results
        ]
    })

@bp.route("/play", methods=["POST"])
async def play():
    data = await request.get_json()
    player_1 = Player.query.filter(Player.name == data["player_1"]).first()
    player_2 = Player.query.filter(Player.name == data["player_2"]).first()
    match = Match(active=False)
    db.session.add(match)
    db.session.commit()
    result = MatchResult(
        winner_move="paper",
        loser_move="rock",
        winner_id=player_1.id,
        loser_id=player_2.id,
        match_id=match.id
    )
    db.session.add(result)
    db.session.commit()
    return jsonify({
        "winner_move": result.winner_move,
        "loser_move": result.loser_move,
        "winner": player_1.name,
        "loser": player_2.name,
        "match_id": match.id
    })
