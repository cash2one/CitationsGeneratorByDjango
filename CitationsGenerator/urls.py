#coding:utf-8
"""
@file:      urls.py
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2016-11-17 14:30
@description:
            存放根路由指向
"""

from django.conf.urls import include, url
from django.contrib import admin

from cite_spider.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^get_store_info',get_store_info),
]
