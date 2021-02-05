from .models import Ad, Advertiser, View, Click
from rest_framework import serializers


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'image_url', 'link', 'approved', 'advertiser']


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['name']


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ['ip', 'time', 'ad']


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['ip', 'time', 'ad']
