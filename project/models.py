from flask_login import UserMixin
from mongoengine import Document,StringField, DateTimeField,ListField
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

class NeoWork(Document):
    name = StringField()
    description = StringField()
    author = StringField()
    creationDate = DateTimeField(default=datetime.datetime.utcnow)
    neoScriptsList = ListField(StringField())
