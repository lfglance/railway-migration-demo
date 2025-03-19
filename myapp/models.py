from datetime import datetime, timezone
from uuid import uuid4

from myapp.factory import db


def get_date():
    return datetime.now(timezone.utc)

def gen_uuid():
    return str(uuid4())


class User(db.Model):
    """
    Users create new projects.
    """
    __tablename__ = "users"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    last_login_date = db.Column(db.DateTime, default=get_date)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.email

class Project(db.Model):
    """
    """
    __tablename__ = "projects"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=False)
    funding_program = db.Column(db.String(100), unique=False, nullable=True)
    funding_amount = db.Column(db.Integer, default=0)
    user_id = db.Column(db.String(200), db.ForeignKey(User.id), nullable=False)
    user = db.relationship("User", backref="projects", foreign_keys=user_id)

    def __repr__(self):
        return self.name

class ProjectRole(db.Model):
    """
    """
    __tablename__ = "project_roles"
    id = db.Column(db.String(200), default=gen_uuid, primary_key=True)
    create_date = db.Column(db.DateTime, default=get_date)
    title = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    hourly_rate = db.Column(db.Integer, unique=False, nullable=False)
    currency = db.Column(db.String(20), default="USD", unique=False, nullable=False)
    project_id = db.Column(db.String(200), db.ForeignKey(Project.id))
    project = db.relationship("Project", backref="roles", foreign_keys=project_id)

    def __repr__(self):
        return self.id
