from abc import ABC, abstractmethod

from django.db import models


class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ad(BaseAdvertising):
    title = models.CharField(max_length=30)
    image_url = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
