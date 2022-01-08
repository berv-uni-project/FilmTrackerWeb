from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'search', views.search, name='search'),
    re_path(r'about', views.about, name='about')
]