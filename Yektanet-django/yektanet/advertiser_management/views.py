from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Advertiser
from .models import Ad
from django.template import loader
from django.utils import timezone


class AdsIndexView(View):
    def get(self, request):
        advertisers = Advertiser.objects.all()
        self.create_views_objects(advertisers, request)
        return render(request, 'advertiser_management/ads.html', {'advertisers': advertisers})

    def create_views_objects(self, advertisers, request):
        user_ip = request.session['user_ip']
        time = timezone.now()
        for advertiser in advertisers:
            for ad in advertiser.ad_set.all():
                ad.view_set.create(ip=user_ip, time=time)
                print(ad.view_set.all())


class AdClickView(View):
    def get(self, request, ad_id):
        ad = Ad.objects.get(pk=ad_id)
        ad.click_set.create(ip=request.session['user_ip'], time=timezone.now())
        print(ad_id)
        return redirect(ad.link)


class CreateAdView(View):
    def get(self, request):
        return render(request, 'advertiser_management/create_ad_form.html', {})


class SubmitAdView(View):
    def post(self, request):
        advertiser_id = request.POST['advertiser_id']
        try:
            advertiser = Advertiser.objects.get(pk=advertiser_id)
        except(ValueError, KeyError, Advertiser.DoesNotExist):
            return render(request, 'advertiser_management/create_ad_form.html', {'error_message': 'Error! Invalid ID!'})
        image_url = request.POST['image_url']
        link = request.POST['link']
        title = request.POST['title']
        if image_url == '' or link == '' or title == '':
            return render(request, 'advertiser_management/create_ad_form.html',
                          {'error_message': 'Error! Blank Inputs Are '
                                            'Invalid!'})
        ad = Ad(title=title, image_url=image_url, link=link, advertiser_id=advertiser_id)
        ad.save()
        return redirect("/ads/")
