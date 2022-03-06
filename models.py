from app import db 
from datetime import datetime
from time import time
import re 

from flask_security import UserMixin, RoleMixin

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s) 

roles_users = db.Table('roles_users',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                    
)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    claim = db.Column(db.Text)
    url = db.Column(db.Text)
    subtitle_full = db.Column(db.String(140))
    subtitle_short = db.Column(db.Text)
    thumnail = db.Column(db.Text)
    rating_tag = db.Column(db.String(140))
    rating_img = db.Column(db.Text)
    rating_text = db.Column(db.String(140))
    author = db.Column(db.String(140))
    date = db.Column(db.String(140))
    true_info = db.Column(db.Text)
    false_info = db.Column(db.Text)
    ctx_info = db.Column(db.Text)
    origin = db.Column(db.Text)
    created = db.Column(db.DateTime,default=datetime.now())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time()))

    def  __repr__(self):
        return f'<Post id: {self.id}, title:{self.id}>'
        
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    roles = db.relationship('Role',secondary=roles_users, 
    backref=db.backref('users'), lazy='dynamic')
    
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)