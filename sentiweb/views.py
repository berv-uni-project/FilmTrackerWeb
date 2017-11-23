from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import SearchForm 
import requests
import json

@require_http_methods(["GET"])
def index(request):
    url_film = 'http://twitter-crawler-data.herokuapp.com/api/popular'
    image_base = 'https://image.tmdb.org/t/p/w500/'
    req = requests.get(url_film)
    jsonData = json.loads(req.text)
    forms = SearchForm()
    return render(request, 'index.html', {'film_data': jsonData['movies'], 'image_base': image_base, 'forms': forms})

@require_http_methods(["POST"])
def search(request):
    url_film = 'http://twitter-crawler-data.herokuapp.com/api/release'
    image_base = 'https://image.tmdb.org/t/p/w500/'
    query = request.POST.get('query', '')
    payload = {'mode': 0, 'query': query}
    req = requests.get(url_film, params=payload)
    jsonData = json.loads(req.text)
    return render(request, 'result.html', {'film_data': jsonData['movies'], 'image_base': image_base})
