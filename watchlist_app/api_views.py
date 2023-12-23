from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from watchlist_app.models import (
    Platform,
    Watchlist
)

from watchlist_app.model_serializers import (
    PlatformSerializer,
    WatchlistSerializer
)


#---------------------------------------------------------------------------
#                              WatchlistAV
#---------------------------------------------------------------------------


class WatchlistAV(APIView):
    """
    API View to perform crud operation on the Watchlist class
    """

#--------------------------------- GET --------------------------------

    def get(self, request, *args, **kwargs):
        if 'pk' in request.query_params:
            try:
                pk = request.query_params['pk']
                instance = Watchlist.objects.get(pk=pk)
                serializer = WatchlistSerializer(instance=instance, many=False)
                return Response(serializer.data, status=200)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
        else:
            instance = Watchlist.objects.all()
            serializer = WatchlistSerializer(instance=instance, many=True)
            return Response(serializer.data, status=200)
        
#--------------------------------- POST --------------------------------

    def post(self, request, *args, **kwargs):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

#--------------------------------- PUT --------------------------------

    def put(self, request, *args, **kwargs):
        data = {
            'message': f"Please enter a correct pk. {str(e)}"
        }

        if 'pk' in request.query_params:
            pk = request.query_params.get('pk')

            try:
                instance = Watchlist.objects.get(pk=int(pk))
            except Exception as e:
                
                return Response(data, status=400)
            
            serializer = WatchlistSerializer(
                instance = instance,
                data = request.data
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response(data, status=400)

#--------------------------------- DELETE --------------------------------

    def delete(self, request):
        data = {
            "message": "Data is deleted."
        }
        if 'pk' in request.query_params:
            pk = request.query_params.get('pk')

            try:
                instance = Watchlist.objects.get(pk=pk)
                instance.delete()
                return Response(data=data, status=204)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
            
        else:
            data = {
                    'message': "Please enter a correct pk"
                }
            return Response(data, status=400)
        

#---------------------------------------------------------------------------
#                            PlatformAV
#---------------------------------------------------------------------------

    
class PlatformAV(APIView):
    """
    API View to perform crud operation on the Platform class
    """
    #--------------------------------- GET --------------------------------
    def get(self, request, *args, **kwargs):
        if 'pk' in request.query_params:
            pk = request.query_params['pk']

            try:
                instance = get_object_or_404(Platform, pk=pk)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
            
            serializer = PlatformSerializer(
                instance = instance,
                many = False,
                context = {'request': request}
            )
            return Response(serializer.data, status=200)

        else:
            instance = Platform.objects.all()
            serializer = PlatformSerializer(
                instance = instance,
                many = True,
                context = {'request': request}
            )
            return Response(serializer.data, status=200)
        
#--------------------------------- POST --------------------------------

    def post(self, request, *args, **kwargs):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

#--------------------------------- PUT --------------------------------

    def put(self, request, *args, **kwargs):
        if 'pk' in request.query_params:
            pk = request.query_params.get('pk')
            try:
                instance = Platform.objects.get(pk=pk)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
            
            serializer = PlatformSerializer(
                instance = instance,
                data = request.data,
                partial = True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        else:
            data = {
                'message': "Please enter a correct pk."
            }
            return Response(data, status=400)

#--------------------------------- DELETE --------------------------------

    def delete(self, request):
        data = {
            "message": "Data is deleted."
        }
        if 'pk' in request.query_params:
            pk = request.query_params.get('pk')
            try:
                instance = Platform.objects.get(pk=pk)
                instance.delete()
                
                return Response(data=data, status=204)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
        else:
            data = {
                    'message': "Please enter a correct pk."
                }
            return Response(data, status=400)
        