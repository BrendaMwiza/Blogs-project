from . import db


class Reader(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.username}'

class Writer(UserMixin,db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))


class Blog(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))


class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
