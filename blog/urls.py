#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url

from views import *

urlpatterns = [
    #url(r"^$", views.blog_index, name="blog_index"),
    url(r"^$", ArticleListView.as_view(), name="blog_index"),
    url(r"^article/publish$", ArticlePublishView.as_view(), name="article_publish"),
    url(r"^article/(?P<title>\w+\.?\w+)$", ArticleDetailView.as_view(), name="article_deatil"),
    url(r"^article/(?P<title>\w+\.?\w+)/edit$", ArticleEditView.as_view(), name="article_edit"),
]
