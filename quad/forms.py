from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class MyRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = [User.USERNAME_FIELD, 'password1', 'password2']
        required_css_class = 'required'
