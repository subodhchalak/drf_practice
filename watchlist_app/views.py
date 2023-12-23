from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from watchlist_app.models import (
    Watchlist
)
from watchlist_app.serializers import (
    WatchlistSerializer
)

# Create your views here.

#---------------------------------------------------------------------------
#                           Watchlist_list
#---------------------------------------------------------------------------


@api_view(['GET', 'POST'])
def watchlist_list(request):
    if request.method == 'GET':
        watchlists = Watchlist.objects.all()
        serializer = WatchlistSerializer(instance=watchlists, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

#---------------------------------------------------------------------------
#                            SECTION HEADER
#---------------------------------------------------------------------------


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def watchlist_details(request, pk):
    if request.method == 'GET':
        watchlist = get_object_or_404(Watchlist, pk=pk)
        serializer = WatchlistSerializer(instance=watchlist, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT' or request.method == 'PATCH':
        watchlist = get_object_or_404(Watchlist, pk=pk)
        serializer = WatchlistSerializer(instance=watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        watchlist = get_object_or_404(Watchlist, pk=pk)
        watchlist.delete()
        data = {
            "message": "Data is deleted."
        }
        return Response(data=data, status=204)

