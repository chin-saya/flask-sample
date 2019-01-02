#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
set FLASK_APP=flaskr/manager
set FLASK_DEBUG=True
flask run
"""

import click
import sqlite3
from contextlib import closing
from flask_migrate import Migrate
from apps import create_app
from exts import db
import models

app = create_app()

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(models=models, db=db)


# 删除指定数据库中的所有表
@app.cli.command()
@click.argument("db_file", default="flaskr.sqlite")
def clear_db(db_file):
    with closing(sqlite3.connect(db_file)) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("select name from sqlite_master where type='table'")
            result = cursor.fetchall()
            print(result)
            try:
                for tb in result:
                    cursor.execute("drop table {}".format(tb[0]))
            except Exception as e:
                print(e.args)

