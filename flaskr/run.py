#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from apps import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
