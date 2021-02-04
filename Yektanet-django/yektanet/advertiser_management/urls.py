
from . import views
from django.urls import path

urlpatterns = [
    path('', views.AdsIndexView.as_view(), name='ads-index'),
    path('<int:ad_id>/', views.AdClickView.as_view(), name='click-ad'),
    path('create_ad/', views.CreateAdView.as_view(), name='create-ad'),
    path('submit/', views.SubmitAdView.as_view(), name='submit-ad'),
]