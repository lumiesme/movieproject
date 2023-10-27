import urllib.parse
from urllib.request import urlopen
import json

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from django.core.paginator import Paginator
from .models import *


class HomeView(TemplateView):
    template_name = 'movieapp/index.html'


class SearchView(TemplateView):
    template_name = 'movieapp/search.html'

class SearchResultView(ListView):
    model = Country
    template_name = 'movieapp/search_result.html'
    table = None



    def get_queryset(self):
        object_list = []
        query = self.request.GET.get('q')
        self.table = self.request.GET.get('table')
        if self.table == 'country':
            object_list = Country.objects.filter(common__icontains=query)
        elif self.table == 'movie':
            value = urllib.parse.quote_plus(query)
            search = 's=' + value
            result = '&'.join([settings.OMDB_URL, search])
            print(result)
            response = urlopen(result)
            data = json.loads(response.read())
            if data['Response'] == 'True':
                for obj in data['Search']:
                    object_list.append(obj)
                    Movie.objects.get_or_create(title=obj['Title'], year=obj['Year'], imdbID=obj['imdbID'],
                                                type=obj['Type'], poster=obj['Poster'])

        return object_list


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = self.table
        return context


class CountryListView(ListView):
    template_name = 'movieapp/country_list.html'
    model = Country
    queryset = Country.objects.order_by('common')
    context_object_name = 'countries'
    paginate_by = 10
    id = 1

class CountryDetailView(DetailView):
    model = Country

class MovieListView(ListView):
    # template_name = 'movieapp/movie_list.html'
    model = Movie
    queryset = Movie.objects.order_by('title')
    context_object_name = 'movies'
    paginate_by = 10
    id = 1

class MovieDetailView(DetailView):
    model = Movie