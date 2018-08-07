#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix="/auth")

from . import view_auth
