from functools import cache

from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Post {}>'.format(self.Title)