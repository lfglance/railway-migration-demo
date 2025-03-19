from datetime import datetime, timezone
from uuid import uuid4

from rps.factory import db


def get_date():
    return datetime.now(timezone.utc)

def gen_uuid():
    return str(uuid4())


class Player(db.Model):
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    last_login_date = db.Column(db.DateTime, default=get_date)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Match(db.Model):
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    active = db.Column(db.Boolean, default=True)

class MatchJoin(db.Model):
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    active = db.Column(db.Boolean, default=True)
    player_id = db.Column(db.String(200), db.ForeignKey(Player.id), nullable=False)
    player = db.relationship("Player", backref="joins", foreign_keys=player_id)
    match_id = db.Column(db.String(200), db.ForeignKey(Match.id), nullable=False)
    match = db.relationship("Match", backref="joins", foreign_keys=match_id)

class MatchResult(db.Model):
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    winner_move = db.Column(db.String(10))
    loser_move = db.Column(db.String(10))
    winner_id = db.Column(db.String(200), db.ForeignKey(Player.id), nullable=False)
    winner = db.relationship("Player", backref="wins", foreign_keys=winner_id)
    loser_id = db.Column(db.String(200), db.ForeignKey(Player.id), nullable=False)
    loser = db.relationship("Player", backref="losses", foreign_keys=loser_id)
    match_id = db.Column(db.String(200), db.ForeignKey(Match.id), nullable=False)
    match = db.relationship("Match", backref="results", foreign_keys=match_id)
