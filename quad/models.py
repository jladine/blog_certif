from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Profil(models.Model):
    avatar = models.FileField(upload_to = 'avatar', null=True, blank =True)

    user = models.OneToOneField(User, unique = True)

    def __unicode__(self):
        return '%s' % (self.user)

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='img_blog')
    is_active = models.BooleanField(default=False)
    # modification_date
    # author = models.ForeignKey(Profil)

    def __unicode__(self):
        return '%s' % (self.title)

class Comment(models.Model):
    body = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Profil)
    article = models.ForeignKey(Article)

class Like(models.Model):
    is_like = models.BooleanField(default=False)

    author = models.ForeignKey(Profil)
    comment = models.ForeignKey(Comment)
