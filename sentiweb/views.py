from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import SearchForm 
from .contributor import Contributor
from .tweetAnalyzer import *
from . import classifier_en
import requests
import json
import sys

@require_http_methods(["GET"])
def index(request):
    # setattr(sys.modules["__main__"], 'stemming_tokenizer', classifier_en.stemming_tokenizer)
    url_film = 'http://twitter-crawler-data.herokuapp.com/api/popular'
    image_base = 'https://image.tmdb.org/t/p/w500/'
    req = requests.get(url_film)
    jsonData = json.loads(req.text)
    result = []
    # jsonData['movies'] = jsonData['movies'][0:1]
    # for movie in jsonData['movies']:
    #     result = analyzeTweet(movie['id'], movie['title'])
    #     jsonData['movies'][movie]['count_pos'] = result['hasil']['count']['pos']
    #     jsonData['movies'][movie]['count_neg'] = result['hasil']['count']['neg']
    #     jsonData['movies'][movie]['count_unk'] = result['hasil']['count']['unk']
        
    forms = SearchForm()
    return render(request, 'index.html', {'film_data': jsonData['movies'],  'image_base': image_base, 'forms': forms})

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
    bervi = Contributor(name='Bervianto Leo Pratama', nim=13514047, image='images/bervi.jpg',facebook='https://facebook.com/bervianto.leo', github='https://github.com/berviantoleo', linkedin='https://www.linkedin.com/in/bervianto-leo-pratama')
    zahid = Contributor(name='M. Az-zahid Adhitya S.', nim=13514095, image='images/zahid-135.jpg')
    luthfi = Contributor(name='Luthfi Kurniawan', nim=13514102, image='images/luthfi.jpg')
    contributors.append(bervi)
    contributors.append(luthfi)
    contributors.append(zahid)
    return render(request, 'about.html', {'contributors': contributors})