#!/usr/bin/env python
# coding=utf-8
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        label = u'username',
        help_text = u'the username to be login.'
        max_length = 20,
        initial = "",
        widget = forms.TextInput(attrs={'class':'form-control'}),
        )

    email = forms.EmailField(
        label = u'email',
        help_text = u'you can login by email.',
        max_length = 50,
        initial = "",
        widget = forms.TextInput(attrs={"class":"form-control"}),
        ) 

    password = forms.CharField(
        label = u'password',
        help_text = u'should be 6-18',
        min_length = 6,
        max_length = 18,
        widget = forms.PasswordInput(attrs={"class":"form-control"}),
        )
    
    confirm_password = forms.CharField(
        label = u'confirm password',
        min_length = 6,
        max_length = 18,
        widget = forms.PasswordInput(attrs={"class":"form-control"}),
        )
