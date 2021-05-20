from database.db import db


class News(db.Document):
    url = db.URLField(required=True, unique=True)
    text = db.StringField(required=True)
    author = db.StringField(required=True)
    posted_date = db.DateTimeField()
    headline = db.StringField(required=True)
    places_mentioned = db.ListField(db.StringField())
    meta = {'collection': 'news_articles'}
