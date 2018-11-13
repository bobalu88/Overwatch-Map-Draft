from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import CreateSessionForm


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
@app.route("/branch")
def branch():
    tournament = session.get('tournament', 'My Tournament')
    team1 = session.get('team1', 'Team 1')
    team2 = session.get('team2', 'Team 2')
    return render_template("branch.html", tournament=tournament, team1=team1, team2=team2)


# Form to create a new draft
@app.route("/form", methods=['GET', 'POST'])
def form():
    form = CreateSessionForm()
    if form.validate_on_submit():
        session['tournament'] = form.tournament.data
        session['team1'] = form.team1.data
        session['team2'] = form.team2.data
        return redirect(url_for('branch'))
    return render_template("form.html", title="Create New Session", form=form)


# Team 1's banning page
@app.route("/team1")
def team1():
    return render_template("team1.html")


# Team 2's banning page
@app.route("/team2")
def team2():
    return render_template("team2.html")


# Spectator
@app.route("/spectator")
def spectator():
    return render_template("spectator.html")


# Admin
@app.route("/admin")
def admin():
    return render_template("admin.html")

