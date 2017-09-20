# -*- coding: utf-8 -*-
from rest_framework import routers

from django.conf.urls import url, include

from reminder.views import ReminderListView, ReminderDetailView


router = routers.DefaultRouter()

router.register(r'reminder/list', ReminderListView, base_name='reminder-list')
router.register(r'reminder/detail', ReminderDetailView, base_name='reminder-detail')

urlpatterns = [
    url(r'', include(router.urls)),
]
