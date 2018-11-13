from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CreateSessionForm(FlaskForm):
    tournament = StringField('Tournament', validators=[DataRequired()])
    team1 = StringField('Team 1', validators=[DataRequired()])
    team2 = StringField('Team 2', validators=[DataRequired()])
    starter = RadioField('First Pick', choices=[('0', 'Random'), ('1', 'Team 1'), ('2', 'Team 2')], validators=[DataRequired()])
    time = IntegerField('Time Limit', validators=[DataRequired()])
    submit = SubmitField('Create Session')
