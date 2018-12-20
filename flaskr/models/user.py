#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from exts import db
from flask_login.mixins import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    _password_hash = db.Column("password", db.String(100), nullable=False)

    articles = db.relationship("Article", backref="author", lazy="dynamic")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password_plain):
        self._password_hash = generate_password_hash(password_plain)

    def verify_password(self, password_plain):
        return check_password_hash(self._password_hash, password_plain)
