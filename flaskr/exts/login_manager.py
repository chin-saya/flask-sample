#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from flask_login import LoginManager
from models import User

login_manager = LoginManager()

"""
请求login_required重定向视图名
1. 如果app使用了蓝图，在blueprint_login_views中查找当前蓝图对应的视图函数
2. 如果app未使用蓝图或当前蓝图未在blueprint_login_views中指定视图函数，则使用login_view配置的视图函数
3. 如果blueprint_login_views中未定义当前蓝图的视图函数，且未定义login_view，则默认抛出401请求错误
"""
login_manager.login_view = "auth.login"
# login_manager.blueprint_login_views = {"blog": "auth.login"}

"""请求login_required默认flash消息"""
login_manager.login_message = "您需要登录后才能访问该页面！"

"""设置flash消息分类，默认为message"""
login_manager.login_message_category = "info"

"""
可设置的值：None, "strong", "basic"
None：禁用session保护机制
basic：持久会话或basic标识的会话。如果hash值不匹配，则设置_fresh=False，标记session为non-fresh。fresh_login_required装饰的视图会强制用户重新验证
strong：strong标识的非持久会话。如果hash值不匹配，则删除session中的'user_id', 'remember', '_id', '_fresh', 'next'
login_manager.session_protection = "strong" 或者SESSION_PROTECTION = "strong"
"""


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user
