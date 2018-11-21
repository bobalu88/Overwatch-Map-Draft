from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


# Create database model
class Tournament(db.Model):
    __tablename__ = "tournaments"
    url = db.Column(db.String(120), primary_key=True, unique=True)
    tournament = db.Column(db.String(120))
    team1 = db.Column(db.String(120))
    team2 = db.Column(db.String(120))
    starter = db.Column(db.String(1))
    time = db.Column(db.Interval)
    timestamp = db.Column(db.DateTime)
    bans = db.Column(db.PickleType)

    def __init__(self, url, tournament, team1, team2, starter, time):
        self.url = url
        self.tournament = tournament
        self.team1 = team1
        self.team2 = team2
        self.starter = starter
        self.time = time

    def __repr__(self):
        return '<URL %r>' % self.url