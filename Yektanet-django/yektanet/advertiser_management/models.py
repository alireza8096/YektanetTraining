from abc import ABC, abstractmethod

from django.db import models
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
