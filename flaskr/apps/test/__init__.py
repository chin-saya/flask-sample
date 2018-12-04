#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Blueprint

test = Blueprint("test", __name__, url_prefix="/test")

from . import view_test