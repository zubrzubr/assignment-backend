# -*- coding: utf-8 -*-
from rest_framework import serializers

from reminder.models import Reminder
from reminder.tasks import send_email_notification


class ReminderBaseSerializer(serializers.ModelSerializer):
    """
    Reminder list serializer for ReminderListView
    """
    # Count of seconds in minute
    SECONDS_COUNT = 60

    class Meta:
        model = Reminder
        fields = ('email', 'delay')

    def create(self, validated_data):
        """
        Override method to send email notification after instance creation
        :param validated_data: validated data from serializer
        :return: created instance
        """
        created = super(ReminderBaseSerializer, self).create(validated_data)
        if created:
            countdown = created.delay * self.SECONDS_COUNT
            send_email_notification.apply_async(countdown=countdown)
        return created


class ReminderDetailSerializer(serializers.ModelSerializer):
    """
    Reminder detail serializer for ReminderDetailView
    """
    class Meta:
        model = Reminder
        fields = ('email', 'delay', 'text')
