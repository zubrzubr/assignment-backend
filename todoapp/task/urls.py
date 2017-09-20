# -*- coding: utf-8 -*-
from rest_framework import routers

from django.conf.urls import url, include

from task.views import TaskListView, TaskDetailView


router = routers.DefaultRouter()

router.register(r'tasks/list', TaskListView, base_name='task-list')
router.register(r'tasks/detail', TaskDetailView, base_name='task-detail')

urlpatterns = [
    url(r'', include(router.urls)),
]
