#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Blueprint

blog = Blueprint('blog', __name__)

from . import view_blog
