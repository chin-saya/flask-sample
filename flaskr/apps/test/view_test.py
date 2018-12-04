#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from . import test
from flask import abort, make_response


@test.route("/exception/401/")
def t_exception():
    abort(401)


@test.route("/make_response/")
def t_make_response():
    response = make_response("return value of test.t_make_response", 403)
    # response = make_response(t_exception())
    response.headers["X-AUTH-TOKEN"] = "token content"
    response.set_cookie("timestamp", "123456")
    return response
