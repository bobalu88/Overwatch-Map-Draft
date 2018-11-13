from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired


# Form to create a new session
class CreateSessionForm(FlaskForm):
    tournament = StringField('Tournament', validators=[DataRequired()])
    team1 = StringField('Team 1', validators=[DataRequired()])
    team2 = StringField('Team 2', validators=[DataRequired()])
    starter = RadioField('First Pick', choices=[('0', 'Random'), ('1', 'Team 1'), ('2', 'Team 2')], validators=[DataRequired()])
    time = IntegerField('Time Limit', validators=[DataRequired()])
    submit = SubmitField('Create Session')
