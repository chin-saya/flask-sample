#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from . import auth
from exts import db
from models import User
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from utils.common import is_safe_url
from werkzeug.exceptions import abort


@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.query.filter(User.username == username).first() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        next = request.args.get("next")
        error = None
        user = User.query.filter(User.username == username).first()

        # 登录验证失败
        if user is None:
            error = 'Incorrect username.'
        elif not user.verify_password(password):
            error = 'Incorrect password.'

        # 登录验证成功
        if error is None:
            login_user(user)
            # 验证next防止重定向攻击
            if not is_safe_url(next):
                abort(400)
            return redirect(next or url_for('blog.index'))

        flash(error)

    return render_template('auth/login.html')


# before_request只能应用到属于蓝本的请求上
# 若要在蓝本中使用针对程序全局请求的钩子，使用before_app_request
# @auth.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')
#
#     if user_id is None:
#         g.user = None
#     else:
#         g.user = User.query.get(user_id)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.index'))
