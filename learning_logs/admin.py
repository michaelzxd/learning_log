#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from django.contrib import admin

from learning_logs.models import Topic, Entry


admin.site.register(Topic)
admin.site.register(Entry)