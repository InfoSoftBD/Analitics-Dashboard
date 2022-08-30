# newspaper_project/urls.py
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
path('admin/', admin.site.urls),
path('users/', include('users.urls')),
path('users/', include('django.contrib.auth.urls')),
path('articles/', include('articles.urls')), # new
path('charts/', include('charts.urls')),
path('', include('charts.urls')), # new
]


