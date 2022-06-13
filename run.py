from app import app
from database import db

db.init_app(app)

#this is used to run the script before the request so that we can create the tables all by ourself
@app.before_first_request
def create_tables():
    db.create_all()
