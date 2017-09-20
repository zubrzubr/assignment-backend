# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                                   CreateModelMixin)

from task.models import Task
from task.serializers import TaskBaseSerializer, TaskDetailSerializer


class TaskListView(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    """
    Task view to get list of all tasks.
    GET, CREATE methods are allowed.
    """
    queryset = Task.objects.all()
    serializer_class = TaskBaseSerializer


class TaskDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    """
    Task detail view to get detail instance of task.
    GET, UPDATE, DELETE methods are allowed.
    """
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskDetailSerializer
