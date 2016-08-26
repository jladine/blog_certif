from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from registration.signals import user_registered

from models import *

User = get_user_model()


class MyRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['email', User.USERNAME_FIELD, 'password1', 'password2']
        required_css_class = 'required'

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        labels = {
            "title": "Titre",
            "body": "Article",
            "is_active": "Actif"
        }


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        labels = {
            "title": "Titre",
            "body": "Article",
            "is_active": "Actif"
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            "author" : forms.HiddenInput(),
            "article" : forms.HiddenInput(),
            }
# 
# class LikeForm(forms.ModelForm):
#     class Meta:
#         model = Like
#         fields = '__all__'
#         widgets = {
#             "author" : forms.HiddenInput(),
#             "comment" : forms.HiddenInput(),
#             }
