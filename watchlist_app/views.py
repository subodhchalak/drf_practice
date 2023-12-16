from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from watchlist_app.models import (
    Movie
)
from watchlist_app.serializer import (
    MovieSerializer
)

# Create your views here.

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(instance=movie, many=False)
    return Response(serializer.data)