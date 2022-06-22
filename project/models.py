from flask_login import UserMixin
from mongoengine import Document,StringField, DateTimeField
import datetime
class User(UserMixin,Document):
    email = StringField()
    password = StringField()
    name = StringField()

class NeoScript(Document):
    name = StringField()
    description = StringField()
    author = StringField()
    date = DateTimeField(default=datetime.datetime.utcnow)
    script = StringField()