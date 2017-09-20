# -*- coding: utf-8 -*-
from rest_framework import serializers

from task.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    """
    Task list serializer for TaskListView
    """
    class Meta:
        model = Task
        fields = ('title', 'status', 'board')


class TaskDetailSerializer(serializers.ModelSerializer):
    """
    Task detail serializer for TaskDetailView
    """
    class Meta:
        model = Task
        fields = ('title', 'status', 'created_date', 'modified_date', 'board')
