#!/usr/bin/env python
# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

from models import *

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, "accounts/register/register.html", {})

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        return HttpResponse(json.dumps("0"))
        #return HttpResponse(json.dumps(username))

