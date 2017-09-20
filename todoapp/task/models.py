# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class Task(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(_('Creation date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modification date'), auto_now=True)

    def __str__(self):
        return self.title
