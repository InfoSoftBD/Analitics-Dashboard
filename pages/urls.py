# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView


#urlpatterns = [
#	path('chartjs/', ChartView.as_view(), name='chart'),
#]

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),

	path('', HomePageView.as_view(), name='homes'),
]