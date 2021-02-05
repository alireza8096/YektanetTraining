from django.db.models import Count
from django.db.models.functions import TruncHour
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from rest_framework.renderers import JSONRenderer
from .models import Advertiser
from .models import Ad, Click
from .models import View as ModelView
from django.template import loader
from django.utils import timezone
from .serializers import AdSerializer


class StatsView(TemplateView):
    template_name = 'advertiser_management/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['click_sum'] = list(get_number_of_clicks_or_views_per_hour_with_id(Click))
        context['view_sum'] = list(get_number_of_clicks_or_views_per_hour_with_id(ModelView))
        context['total_click_per_view'] = Click.objects.count() / ModelView.objects.count()
        context['average_delta_click_and_view'] = get_average_delta_click_and_time()
        context['click_per_view_rate_per_hour'] = get_click_per_view_rate_per_hour()
        return context


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
                # print(ad.view_set.all())


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


def get_number_of_clicks_or_views_per_hour_with_id(model):
    return model.objects.annotate(hour_and_date=TruncHour('time')).values('ad_id', 'hour_and_date') \
        .annotate(repeat=Count('ad_id')).values('ad_id', 'hour_and_date', 'repeat')


def get_delta_view_and_click(click_id):
    click = Click.objects.get(pk=click_id)
    view = ModelView.objects.filter(ip=click.ip, ad_id=click.ad_id, time__lt=click.time).order_by('-time')[0]
    return click.time - view.time


def get_average_delta_click_and_time():
    clicks_num = Click.objects.count()
    delta = timezone.now()
    for click in Click.objects.all():
        delta += get_delta_view_and_click(click.id)
    delta -= timezone.now()
    print(delta / clicks_num)
    get_click_per_view_rate_per_hour()
    return delta / clicks_num


def get_number_of_clicks_or_views_per_hour_without_id(model):
    return model.objects.annotate(hour_and_date=TruncHour('time')).values('hour_and_date') \
        .annotate(repeat=Count('hour_and_date')).values('hour_and_date', 'repeat').order_by('hour_and_date')


def get_list_of_hours_for_model(model):
    return model.objects.annotate(hour_and_date=TruncHour('time')).values('hour_and_date') \
        .annotate(repeat=Count('hour_and_date')).values('hour_and_date').order_by('hour_and_date')


def get_click_per_view_rate_per_hour():
    clicks_list = list(get_number_of_clicks_or_views_per_hour_without_id(Click))
    view_list = list(get_number_of_clicks_or_views_per_hour_without_id(ModelView))
    clicks_hour_list = list(get_list_of_hours_for_model(Click))
    view_hour_list = list(get_list_of_hours_for_model(ModelView))
    final_list = []
    for time in view_hour_list:
        if time in clicks_hour_list:
            rate = clicks_list[clicks_hour_list.index(time)]['repeat'] / view_list[view_hour_list.index(time)]['repeat']
            final_list.append({'date': time['hour_and_date'], 'rate': rate})
    print(final_list)
    return final_list
