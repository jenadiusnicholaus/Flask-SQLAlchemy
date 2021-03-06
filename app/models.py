from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    user_email = db.Column(db.String(128), nullable=False)
    user_password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username