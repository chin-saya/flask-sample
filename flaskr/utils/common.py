#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from urllib.parse import urlparse, urljoin
from flask import request


def is_safe_url(target):
    # ref_url: ParseResult(scheme='http', netloc='127.0.0.1:5000', path='/', params='', query='', fragment='')
    ref_url = urlparse(request.host_url)

    # test_url: ParseResult(scheme='http', netloc='127.0.0.1:5000', path='/create', params='', query='', fragment='')
    test_url = urlparse(urljoin(request.host_url, target))

    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
