#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from celery import Celery

celery = Celery(__name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0")


@celery.task
def add(x, y):
    return x + y
