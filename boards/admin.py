# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from boards.models import Choice, Poll, Vote

admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)