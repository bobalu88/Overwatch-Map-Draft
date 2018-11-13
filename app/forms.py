from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CreateSessionForm(FlaskForm):
    tournament = StringField('Tournament')
    team1 = StringField('Team 1')
    team2 = StringField('Team 2')
    starter = RadioField('First Pick', choices=[('0', 'Random'), ('1', 'Team 1'), ('2', 'Team 2')])
    time = IntegerField('Time Limit')
    submit = SubmitField('Create Session')
