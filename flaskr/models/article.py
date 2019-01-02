#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from exts import db
from flask_login.mixins import UserMixin
from datetime import datetime
from sqlalchemy import ForeignKey


class Article(db.Model, UserMixin):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    created_time = db.Column(db.DATETIME, nullable=False, default=datetime.now)
    author_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
