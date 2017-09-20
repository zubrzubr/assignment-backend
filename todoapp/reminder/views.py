# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                                   CreateModelMixin)

from reminder.models import Reminder
from reminder.serializers import ReminderBaseSerializer, ReminderDetailSerializer


class ReminderListView(ListModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    """
    Reminder view to get list of all reminders.
    GET, CREATE methods are allowed.
    """
    queryset = Reminder.objects.all()
    serializer_class = ReminderBaseSerializer


class ReminderDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    """
    Reminder detail view to get detail instance of reminder.
    GET, UPDATE, DELETE methods are allowed.
    """
    queryset = Reminder.objects.all()
    lookup_field = 'id'
    serializer_class = ReminderDetailSerializer
