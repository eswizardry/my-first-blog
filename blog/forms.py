#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mcsbanch
# @Date:   2016-02-06 16:37:48
# @Last Modified by:   mcsbanch
# @Last Modified time: 2016-02-06 16:38:03
from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
