#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcsbanch
# @Date:   2016-02-06 13:17:31
# @Last Modified by:   mcsbanch
# @Last Modified time: 2016-02-06 17:00:00
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
