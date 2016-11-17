#coding:utf-8
"""
@file:      urls.py
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    2.7
@editor:    PyCharm
@create:    2016-11-17 14:30
@description:
            存放根路由指向
"""

from django.conf.urls import include, url
from django.contrib import admin

from spider.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_store_info',get_store_info),
]

'''
    test url:
        http://127.0.0.1:8000/get_store_info?store_url=https://detail.tmall.com/item.htm?id=538059530916&spm=a219t.7900221/10.1998910419.d30ccd691.YF4fJI
        http://127.0.0.1:8000/get_page_num?products_url=https://qyxcy.tmall.com/search.htm?search=y&orderType=newOn_desc&tsearch=y
        http://127.0.0.1:8000/get_products_info?products_url=https://qyxcy.tmall.com/search.htm?search=y&orderType=newOn_desc&tsearch=y
        http://127.0.0.1:8000/get_daren_prods?daren_url=http://ku.uz.taobao.com/
        http://127.0.0.1:8000/random_kick?start=5732587480&end=5732588480&dynamic_range_length=1000&mysql=1
'''