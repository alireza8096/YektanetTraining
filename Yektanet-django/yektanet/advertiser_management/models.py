from abc import ABC, abstractmethod

from django.db import models


class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def inc_clicks(self):
        self.clicks += 1
        self.save()

    def inc_views(self):
        self.views += 1
        self.save()


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ad(BaseAdvertising):
    title = models.CharField(max_length=30)
    image_url = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)

    def inc_clicks(self):
        super().inc_clicks()
        self.advertiser.inc_clicks()

    def inc_views(self):
        super().inc_views()
        self.advertiser.inc_views()

    def __str__(self):
        return self.title
