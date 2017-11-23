from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import SearchForm 
from .contributor import Contributor
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

@require_http_methods(["GET"])
def about(request):
    contributors = []
    bervi = Contributor(name='Bervianto Leo Pratama', nim=13514047, image='images/bervi-135.jpg',facebook='https://facebook.com/bervianto.leo', github='https://github.com/berviantoleo', linkedin='https://www.linkedin.com/in/bervianto-leo-pratama')
    zahid = Contributor(name='M. Az-zahid Adhitya S.', nim=13514095, image='images/zahid-135.jpg')
    luthfi = Contributor(name='Luthfi Kurniawan', nim=13514102, image='images/luthfi-135.jpg')
    contributors.append(bervi)
    contributors.append(luthfi)
    contributors.append(zahid)
    return render(request, 'about.html')
