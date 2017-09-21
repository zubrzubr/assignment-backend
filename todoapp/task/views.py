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
    Also can urls can be applied, for example:
    ?is_done=true, ?board_name=TestBoard
    """
    serializer_class = TaskBaseSerializer

    def get_queryset(self):
        queryset = Task.objects
        is_done_param = self.request.GET.get('is_done')
        board_name_param = self.request.GET.get('board_name')

        query_params = {
            'status': bool(is_done_param),
        }

        if board_name_param:
            query_params.update({'board__name': board_name_param})
        if is_done_param or board_name_param:
            return queryset.filter(**query_params)

        return queryset


class TaskDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    """
    Task detail view to get detail instance of task.
    GET, UPDATE, DELETE methods are allowed.
    """
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskDetailSerializer
