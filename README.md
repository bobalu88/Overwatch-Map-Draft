How to run:

in final:
set FLASK_APP=final.py
flask run

heroku:
heroku run python
from app.model import db
db.drop_all()  # to reset
db.create_all()