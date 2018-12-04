#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask import Flask
import config


def create_app():
    # static_url_path-->C:\\Users\\admin\\Desktop\\PycharmProjects\\flask_example
    # app = Flask(__name__, static_url_path="")

    # static_url_path-->C:\\static
    # app = Flask(__name__, static_url_path="/static")

    app = Flask(__name__)
    # print(">>>", app.name)  # apps
    # print(">>>", app.instance_path)  # C:\Users\admin\Desktop\PycharmProjects\flask_example\instance
    # print(">>>", app.root_path)  # C:\Users\admin\Desktop\PycharmProjects\flask_example\flaskr
    app.config.from_object(config)

    from exts import db
    db.init_app(app)
    from exts import login_manager
    login_manager.init_app(app)
    from .blog import blog
    app.register_blueprint(blog)
    from .auth import auth
    app.register_blueprint(auth)
    from .test import test
    app.register_blueprint(test)
    from exceptions import exception
    app.register_blueprint(exception)

    return app
