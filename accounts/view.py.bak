#!/usr/bin/env python
# coding=utf-8

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from forms import RegisterForm


class RegisterView(FormView):
    """
    register the new user
    """
    #template_name = "accounts/register.html"
    template_name = "accounts/register/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('blog_index')

    #def form_valid(self, form):
    #    form.save()
    #    username = form.cleaned_data.get('username')
    #    password = form.cleaned_data.get('password')
    #    user = authenticate(username=username, password=password)
    #    login(self.request, user)
    #    return super(RegisterView, self).form_valid(form)


