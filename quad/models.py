from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Profil(models.Model):
    avatar = models.FileField(upload_to = 'avatar', null=True, blank =True)

    user = models.OneToOneField(User, unique = True, related_name="profil_set")

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

    def __unicode__(self):
        return '%s' % (self.body)

class Like(models.Model):
    author = models.ForeignKey(Profil)
    comment = models.ForeignKey(Comment, related_name="like_set")


@receiver(post_save, sender=User)
def create_user_profil(sender, instance, created, **kwargs):
    if created:
            Profil.objects.create(user=instance)
