
from . import views
from django.urls import path

urlpatterns = [
    path('', views.ads_index, name='ads-index'),
]