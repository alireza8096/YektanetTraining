from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertiser
from .models import Ad
from django.template import loader


def ads_index(request):
    advertisers = Advertiser.objects.all()
    inc_list_views(advertisers)
    return render(request, 'advertiser_management/ads.html', {'advertisers': advertisers})


def click_ad(request, ad_id):
    ad = Ad.objects.get(pk=ad_id)
    ad.inc_clicks()
    return redirect(ad.link)


def inc_list_views(advertisers):
    for advertiser in advertisers:
        for ad in advertiser.ad_set.all():
            ad.inc_views()


def create_ad(request):
    return render(request, 'advertiser_management/create_ad_form.html', {})


def submit(request):
    advertiser_id = request.POST['advertiser_id']
    try:
        advertiser = Advertiser.objects.get(pk=advertiser_id)
    except(ValueError, KeyError, Advertiser.DoesNotExist):
        return render(request, 'advertiser_management/create_ad_form.html', {'error_message': 'Error! Invalid ID!'})
    image_url = request.POST['image_url']
    link = request.POST['link']
    title = request.POST['title']
    if image_url == '' or link == '' or title == '':
        return render(request, 'advertiser_management/create_ad_form.html', {'error_message': 'Error! Blank Inputs Are '
                                                                                              'Invalid!'})
    ad = Ad(title=title, image_url=image_url, link=link, advertiser_id=advertiser_id)
    ad.save()
    return redirect("http://127.0.0.1:8000/ads/")
