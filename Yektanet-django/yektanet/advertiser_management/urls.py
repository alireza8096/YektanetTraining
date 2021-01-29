
from . import views
from django.urls import path

urlpatterns = [
    path('', views.ads_index, name='ads-index'),
    path('<int:ad_id>/', views.click_ad, name='click-ad'),
    path('create_ad/', views.create_ad, name='create-ad'),
    path('submit/', views.submit, name='submit-ad'),
]