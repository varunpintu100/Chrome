from database import db
from sqlalchemy import func

class IMG(db.Model):

    __tablename__='Images'

    #We are creating the coloumns for the table in the database

    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.Text,unique=True,nullable=False)
    Xpath=db.Column(db.Text,nullable=False)
    Name=db.Column(db.Text,nullable=False)
    RunId = db.Column(db.Integer,nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()

    def Get_runID(self):
        results = db.session.query(func.max('Images'.RunId)).all()
        if results is None:
            return 0
        return results