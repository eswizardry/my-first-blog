#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcsbanch
# @Date:   2016-02-06 13:17:31
# @Last Modified by:   mcsbanch
# @Last Modified time: 2016-02-06 13:18:42
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
