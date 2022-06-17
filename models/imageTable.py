from enum import unique
from database import db


class IMG(db.Model):
    __tablename__='Images'

    #We are creating the coloumns for the table in the database

    id=db.Column(db.Integer,primary_key=True)
    img=db.Column(db.Text,unique=True,nullable=False)
    Xpath=db.Column(db.Text,nullable=False)
    mimetype=db.Column(db.Text,nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()
