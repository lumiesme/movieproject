from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('country_list/', views.CountryListView.as_view(), name='country_list'),  # Country View
    path('country_detail/<int:pk>', views.CountryDetailView.as_view(), name='country_detail'),
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),  # Country View
    path('movie_detail/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('search/', views.SearchView.as_view(), name="search"),
    path('search_result/', views.SearchResultView.as_view(), name="search_result")
]