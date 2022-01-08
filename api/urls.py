from django.urls import re_path

from . import views

urlpatterns = [
	re_path(r'^search', views.search, name='search'),
	re_path(r'^savesearch', views.save, name='save'),
	re_path(r'^release', views.retrieve_movie, name='release'),
	re_path(r'^saverelease', views.movie_list, name='saverelease'),
	re_path(r'^popular', views.retrieve_popular, name='popular'),
	re_path(r'^savemovie', views.search_movie, name='savemovie'),
	re_path(r'^savepopular', views.popular_movie, name='savepopular'),
	re_path(r'^traindata', views.traindata, name='traindata')
]
