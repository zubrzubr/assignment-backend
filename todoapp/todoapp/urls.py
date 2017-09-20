# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api/v1/', include('board.urls')),
    url(r'^api/v1/', include('task.urls')),
    url(r'^api/v1/', include('reminder.urls')),
    url(r'^admin/', admin.site.urls),
]
