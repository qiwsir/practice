from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    url = models.URLField()
    title = models.CharField(max_length = 50)
    title_zh = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30)
    content_md = models.TextField()
    content_html = models.TextField()
    tags = models.CharField(max_length = 30)
    views = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
