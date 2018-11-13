from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import CreateSessionForm


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/branch")
def branch():
    return render_template("branch.html")


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = CreateSessionForm()
    if form.validate_on_submit():
        flash('Session requested for tournament {}, team1={}, team2={}, starter={}, time={}'.format(
            form.tournament.data, form.team1.data, form.team2.data, form.starter.data, form.time.data))
        return redirect(url_for('branch'))
    return render_template("form.html", title="Create New Session", form=form)


@app.route("/team1")
def team1():
    return render_template("team1.html")


@app.route("/team2")
def team2():
    return render_template("team2.html")


@app.route("/spectator")
def spectator():
    return render_template("spectator.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")

