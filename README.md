How to run:

in final:
set FLASK_APP=final.py
flask run

heroku:
heroku run python
from app import db
db.create_all()
exit()