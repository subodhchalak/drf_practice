from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from watchlist_app.models import (
    Watchlist,
    Platform,
    Review
)
from watchlist_app.generic_serializers import (
    WatchlistSerializer,
    PlatformSerializer,
    ReviewSerializer
)


#---------------------------------------------------------------------------
#                            WatchlistVS
#---------------------------------------------------------------------------

class WatchlistVS(viewsets.ViewSet):
    def list(self, request):
        queryset = Watchlist.objects.all()
        serializer = WatchlistSerializer(
            instance = queryset,
            many = True,
            context = {'request': request}
        )
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Watchlist, pk=pk)
        serializer = WatchlistSerializer(
            instance = queryset,
            many = False,
            context = {'request': request}
        )
        return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        serializer = WatchlistSerializer(
            data = data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
        
    def update(self, request, pk=None):
        instance = get_object_or_404(Watchlist, pk=pk)
        data = request.data
        serializer = WatchlistSerializer(
            instance = instance,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
        
    def destroy(self, request, pk=None):
        instance = get_object_or_404(Watchlist, pk=pk)
        instance.delete()
        return Response(status=204)
        

#---------------------------------------------------------------------------
#                            PlatformMV
#---------------------------------------------------------------------------

class PlatformMV(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer