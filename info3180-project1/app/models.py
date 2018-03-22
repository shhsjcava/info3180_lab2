from . import db


class User(db.Model):
    userid = db.Column(db.String, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    sex=db.Column(db.String(10))
    address=db.Column(db.String(150))
    email=db.Column(db.String(120))
    bio=db.Column(db.String(255))
    photo=db.Column(db.String(255))
    joined=db.Column(db.String(80))
    

    def __init__(self, userid, fname, lname, sex, address, email, bio, photo, date):
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.sex=sex
        self.address=address
        self.email=email
        self.bio=bio
        self.photo=photo
        self.joined=date

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r>' %  self.username