# -*- coding: utf-8 -*-
from rest_framework import routers

from django.conf.urls import url, include

from board.views import BoardListView, BoardDetailView


router = routers.DefaultRouter()

router.register(r'board/list', BoardListView, base_name='board-list')
router.register(r'board/detail', BoardDetailView, base_name='board-detail')

urlpatterns = [
    url(r'', include(router.urls)),
]
