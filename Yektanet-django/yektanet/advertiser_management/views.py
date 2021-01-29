from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertiser
from .models import Ad
from django.template import loader


def ads_index(request):
    advertisers = Advertiser.objects.all()
    inc_list_views(advertisers)
    template = loader.get_template('advertiser_management/ads.html')
    context = {
        'advertisers': advertisers
    }
    return HttpResponse(template.render(context, request))


def click_ad(request, ad_id):
    ad = Ad.objects.get(pk=ad_id)
    ad.inc_clicks()
    print(ad.clicks)
    return redirect(ad.link)


def inc_list_views(advertisers):
    for advertiser in advertisers:
        for ad in advertiser.ad_set.all():
            ad.inc_views()
