# -*- coding: utf-8 -*-
from rest_framework import serializers

from board.models import Board


class BoardListSerializer(serializers.ModelSerializer):
    """
    Board list serializer for BoardListView
    """
    todo_count = serializers.SerializerMethodField('get_tasks_count')

    class Meta:
        model = Board
        fields = ('name', 'todo_count')

    @staticmethod
    def get_tasks_count(obj):
        """
        Returns count of tasks related to board
        :param obj: Model object 
        :return: int count of board tasks
        """
        return obj.board_tasks.count()


class BoardDetailSerializer(serializers.ModelSerializer):
    """
    Board detail serializer for BoardDetailView
    """
    board_tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = Board
        fields = ('name', 'board_tasks')
