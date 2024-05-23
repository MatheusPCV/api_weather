from django import forms
from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import UserEntity

class UserForm(forms.Form):
    username = forms.CharField(max_length=150)
    id = forms.IntegerField(required=False)
    name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)