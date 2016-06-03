#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url
#from views import RegisterView


urlpatterns = [
    #url(r"^register/", RegisterView.as_view(), name="register"),
    url(r"^register/", "accounts.views.register", name="register"),
]
