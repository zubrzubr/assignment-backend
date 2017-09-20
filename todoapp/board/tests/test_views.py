# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import simplejson

from django.core.urlresolvers import reverse


@pytest.mark.django_db
class TestBoardListView(object):
    def test_post_should_create_new_board(self, client):
        list_url = reverse('board-list-list')
        params = {
            'name': 'Test Board'
        }

        resp = simplejson.loads(client.post(list_url, params).content)
        expected_resp = {u'name': u'Test Board', u'todo_count': 0}

        assert resp == expected_resp

    def test_post_should_not_create_new_board_if_no_required_field(self, client):
        list_url = reverse('board-list-list')
        params = {
            'name': ''
        }

        resp = simplejson.loads(client.post(list_url, params).content)
        expected_resp = {u'name': ['This field may not be blank.']}

        assert resp == expected_resp
