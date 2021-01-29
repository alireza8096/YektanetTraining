from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertiser
from .models import Ad
from django.template import loader


def ads_index(request):
    advertisers = Advertiser.objects.all()
    for advertiser in advertisers:
        for ad in advertiser.ad_set.all():
            ad.inc_views()
    template = loader.get_template('advertiser_management/ads.html')
    context = {
        'advertisers': advertisers
    }
    return HttpResponse(template.render(context, request))
