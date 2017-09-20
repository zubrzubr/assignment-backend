# -*- coding: utf-8 -*-
from rest_framework import serializers

from reminder.models import Reminder


class ReminderBaseSerializer(serializers.ModelSerializer):
    """
    Reminder list serializer for ReminderListView
    """
    class Meta:
        model = Reminder
        fields = ('email', 'delay')


class ReminderDetailSerializer(serializers.ModelSerializer):
    """
    Reminder detail serializer for ReminderDetailView
    """
    class Meta:
        model = Reminder
        fields = ('email', 'delay', 'text')
