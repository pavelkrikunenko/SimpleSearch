from Search import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    rubrics = db.Column(db.Text)