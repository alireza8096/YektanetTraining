from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.AdsIndexView.as_view(), name='ads-index'),
    path('<int:ad_id>/', views.AdClickView.as_view(), name='click-ad'),
    path('create_ad/', views.CreateAdView.as_view(), name='create-ad'),
    path('submit/', views.SubmitAdView.as_view(), name='submit-ad'),
    path('stats/', views.StatsView.as_view(), name='stats-view'),

]

router = DefaultRouter()
router.register(r'ads_view_set', views.AdViewSet, basename='user')
urlpatterns += router.urls

