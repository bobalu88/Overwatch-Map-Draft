from app import app
from flask_sqlalchemy import SQLAlchemy
import datetime
from app.utils import create_map_list


# Create database model
class Tournament(app.db.Model):
    __tablename__ = "tournaments"
    url = app.db.Column(app.db.String(120), primary_key=True, unique=True)
    tournament = app.db.Column(app.db.String(120))
    team1 = app.db.Column(app.db.String(120))
    team2 = app.db.Column(app.db.String(120))
    starter = app.db.Column(app.db.String(1))
    time = app.db.Column(app.db.Interval)
    timestamp = app.db.Column(app.db.DateTime)
    bans = app.db.Column(app.db.PickleType)

    def __init__(self, url, tournament, team1, team2, starter, time):
        self.url = url
        self.tournament = tournament
        self.team1 = team1
        self.team2 = team2
        self.starter = starter
        self.time = time
        self.timestamp = datetime.now()
        self.bans = create_map_list()

    def __repr__(self):
        return '<URL %r>' % self.url
