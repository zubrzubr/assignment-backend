# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Reminder(models.Model):
    email = models.EmailField(_('Email'))
    text = models.TextField(_('Reminder text'), max_length=512)
    delay = models.IntegerField(_('Reminder delay'))

    def __str__(self):
        return self.email
