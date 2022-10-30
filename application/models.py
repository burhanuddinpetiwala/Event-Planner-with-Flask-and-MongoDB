from enum import unique
import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    user_id = db.IntField( unique=True )
    First_Name = db.StringField( max_length = 50 )
    Last_Name = db.StringField( max_length = 50 )
    Email = db.StringField (max_length = 153)
    Password = db.StringField ()

    def set_password(self, password):
        self.Password = generate_password_hash(password)
    
    def get_password(self, password):
        return check_password_hash(self.Password, password)

class Event(db.Document):
    user_id = db.IntField()
    event_id = db.IntField( max_length = 10)
    Event_Name = db.StringField( max_length = 100)
    Event_Date = db.DateField( max_length = 255)
