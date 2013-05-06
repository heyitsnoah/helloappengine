from google.appengine.ext import db

class Name(db.Model):
    name = db.StringProperty()