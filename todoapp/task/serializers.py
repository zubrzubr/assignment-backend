# -*- coding: utf-8 -*-
from rest_framework import serializers

from task.models import Task


class TaskBaseSerializer(serializers.ModelSerializer):
    """
    Task list serializer for TaskListView
    """
    board = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ('title', 'status', 'board')


class TaskDetailSerializer(TaskBaseSerializer):
    """
    Task detail serializer for TaskDetailView
    """
    class Meta:
        model = Task
        fields = ('title', 'status', 'created_date', 'modified_date', 'board')
