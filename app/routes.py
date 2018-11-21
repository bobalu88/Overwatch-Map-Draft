from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import CreateSessionForm
from app.utils import sanitize

# Home page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Index")


# About the site
@app.route("/about")
def about():
    return render_template("about.html")


# Links to each team, etc
@app.route("/branch/<page>")
def branch(page):
    tournament = session.get('tournament', 'My Tournament')
    team1 = session.get('team1', 'Team 1')
    team2 = session.get('team2', 'Team 2')
    return render_template("branch.html", tournament=tournament, team1=team1, team2=team2)


# Form to create a new draft
@app.route("/form", methods=['GET', 'POST'])
def form():
    form = CreateSessionForm()
    if form.validate_on_submit():
        tournament = form.tournament.data
        team1 = form.team1.data
        team2 = form.team2.data
        starter = form.starter.data
        time = form.time.data
        url = sanitize(form.tournament.data)
        if not app.db.session.query(app.Tournament).filter(app.Tournament.url == url).count():
            curr = app.Tournament(url, tournament, team1, team2, starter, time)
            app.db.session.add(curr)
            app.db.session.commit()
            return redirect(url_for('branch', page=url))
    return render_template("form.html", title="Create New Session", form=form)


# Team 1's banning page
@app.route("/team1/<page>")
def team1(page):
    return render_template("team1.html")


# Team 2's banning page
@app.route("/team2/<page>")
def team2(page):
    return render_template("team2.html")


# Spectator
@app.route("/spectator/<page>")
def spectator(page):
    return render_template("spectator.html")


# Admin
@app.route("/admin/<page>")
def admin(page):
    return render_template("admin.html")

