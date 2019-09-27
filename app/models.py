from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from flask_login import UserMixin,login_required
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Writer(UserMixin,db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'writer', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'writer', lazy = "dynamic")


class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'blog', lazy = "dynamic")

    all_blogs = []
    
    def __init__(self,title,body):
        self.title = title
        self.body = body
        

    def save_blog(self):
        '''
        Save blogs
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_blogs(cls):
        blog.all_blogs.clear()

    def get_blogs(id):
        blogs = Blog.query.filter_by(title_id=id).all()
        return blogs


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))


class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
