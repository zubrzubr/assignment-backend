# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from task.models import Task


class Board(models.Model):
    name = models.CharField(_('Board name'), max_length=255)
    tasks = models.ForeignKey(Task, related_name='board_tasks')

    def __str__(self):
        return self.name
