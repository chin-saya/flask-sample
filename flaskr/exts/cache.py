#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
CACHE_TYPE:

CACHE_DEFAULT_TIMEOUT: 默认300.
CACHE_THRESHOLD: 默认500。
CACHE_KEY_PREFIX: 默认"flask_cache_"
CACHE_MEMCACHED_SERVERS: 默认None。
CACHE_DIR: 默认None。
CACHE_OPTIONS: 默认None。
CACHE_ARGS: 默认[]。
CACHE_TYPE: 默认"null"。
CACHE_NO_NULL_WARNING: 默认False。当CACHE_TYPE为"null"时，显示警告信息

CACHE_REDIS_HOST:
CACHE_REDIS_PORT:
CACHE_REDIS_PASSWORD:
CACHE_REDIS_DB:
CACHE_REDIS_URL:

"""

from flask_caching import Cache

config = {'CACHE_TYPE': 'simple'}

cache = Cache(config=config)
