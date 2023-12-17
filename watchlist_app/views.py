from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from watchlist_app.models import (
    Movie
)
from watchlist_app.serializer import (
    MovieSerializer
)

# Create your views here.

#---------------------------------------------------------------------------
#                           movie_list
#---------------------------------------------------------------------------


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance=movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            print(f"Data: {serializer.data}")
            # serializer.save()
            return Response(serializer.data)
        else:
            print(f"Errors: {serializer.errors}")
            return Response(serializer.errors, status=400)
        

#---------------------------------------------------------------------------
#                            SECTION HEADER
#---------------------------------------------------------------------------


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(instance=movie, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT' or request.method == 'PATCH':
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        data = {
            "message": "Data is deleted."
        }
        return Response(data=data, status=204)

