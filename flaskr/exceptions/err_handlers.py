#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Blueprint

exception = Blueprint("exception", __name__)


# 使用app_errorhandler进行全局异常处理
@exception.app_errorhandler(401)
def error_401(e):
    return "error 401", 401
