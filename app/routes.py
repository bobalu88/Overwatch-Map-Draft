from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import CreateSessionForm
from app.utils import sanitize
from app.model import Tournament, db


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
@app.route("/<page>/branch")
def branch(page):
    tournament = 'My Tournament'
    team1 = 'Team 1'
    team2 = 'Team 2'
    try:
        query = db.session.query(Tournament).filter(Tournament.url == page).first()
        tournament = query.tournament
        team1 = query.team1
        team2 = query.team2
    except:
        flash("Something went wrong")
    return render_template("branch.html", tournament=tournament, team1=team1, team2=team2, url=page)


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
        session['tournament'] = tournament
        session['team1'] = team1
        session['team2'] = team2
        if not db.session.query(Tournament).filter(Tournament.url == url).count():
            curr = Tournament(url, tournament, team1, team2, starter, time)
            db.session.add(curr)
            db.session.commit()
        return redirect(url_for('branch', page=url))
    return render_template("form.html", title="Create New Session", form=form)


# Team 1's banning page
@app.route("/<page>/team1")
def team1(page):
    tournament = 'My Tournament'
    team1 = 'Team 1'
    team2 = 'Team 2'
    query = {}
    try:
        query = db.session.query(Tournament).filter(Tournament.url == page).first()
        tournament = query.tournament
        team1 = query.team1
        team2 = query.team2
    except:
        flash("Something went wrong")
    return render_template("team1.html", query=query)


# Team 2's banning page
@app.route("/<page>/team2")
def team2(page):
    return render_template("team2.html")


# Spectator
@app.route("/<page>/spectator")
def spectator(page):
    return render_template("spectator.html")


# Admin
@app.route("/<page>/admin")
def admin(page):
    return render_template("admin.html")

