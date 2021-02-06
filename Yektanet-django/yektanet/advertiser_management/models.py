from abc import ABC, abstractmethod
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Advertiser(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Click(models.Model):
    ip = models.CharField(max_length=20)
    time = models.DateTimeField(default=timezone.now())
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class View(models.Model):
    ip = models.CharField(max_length=20)
    time = models.DateTimeField(default=timezone.now())
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class HourReport(models.Model):
    date = models.DateTimeField()
    clicks = models.IntegerField()
    views = models.IntegerField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)