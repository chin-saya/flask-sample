#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# set FLASK_APP=flaskr
# set FLASK_DEBUG=True
# python3 flaskr/manager.py shell
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

"""被login_required拦截的请求地址（request.path），会以查询字符串next=?的方式被传递给重定向视图，从而登录成功后直接访问。
或者，通过设置USE_SESSION_FOR_NEXT将next添加到session而非url

USE_SESSION_FOR_NEXT = True
"""

# session配置
SECRET_KEY = "dev"

# 数据库配置
SQLALCHEMY_DATABASE_URI = r'sqlite:///{}{}flaskr.sqlite'.format(BASE_DIR, os.sep)
SQLALCHEMY_TRACK_MODIFICATIONS = False
