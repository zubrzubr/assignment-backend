# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                                   CreateModelMixin)

from board.models import Board
from board.serializers import BoardListSerializer, BoardDetailSerializer


class BoardListView(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    """
    Board view to get list of all boards and count of tasks in this board.
    GET, CREATE methods are allowed.
    Response:
        [
            {
                "name": "Test",
                "todo_count": 2
            }
        ]
    """
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer


class BoardDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    """
    Board detail view to get detail instance of board.
    GET, UPDATE, DELETE methods are allowed.
    """
    queryset = Board.objects.all()
    lookup_field = "id"
    serializer_class = BoardDetailSerializer
