from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from watchlist_app.models import Movie
from watchlist_app.serializer import MovieSerializer


#---------------------------------------------------------------------------
#                            MovieListAV
#---------------------------------------------------------------------------

class MovieListAV(APIView):
    """
    API View to perform crud operation on the Movie clas
    """

#--------------------------------- GET --------------------------------

    def get(self, request, *args, **kwargs):
        if 'pk' in request.query_params:
            pk = request.query_params['pk']
            print(f"PK: {pk}")
            try:
                movie = get_object_or_404(Movie, pk=pk)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
            
            serializer = MovieSerializer(instance=movie, many=False)
            return Response(serializer.data, status=200)

        else:
            movie = Movie.objects.all()
            serializer = MovieSerializer(instance=movie, many=True)
            return Response(serializer.data, status=200)
        
#--------------------------------- POST --------------------------------

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
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
                movie = Movie.objects.get(pk=pk)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
            serializer = MovieSerializer(instance=movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)

#--------------------------------- patch --------------------------------

    def patch(self, request):
        if 'pk' in request.query_params:
            pk = request.query_params.get('pk')
            try:
                movie = Movie.objects.get(pk=pk)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
                            
            serializer = MovieSerializer(instance=movie, data=request.data)
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
                movie = Movie.objects.get(pk=pk)
                movie.delete()
                
                return Response(data=data, status=204)
            except Exception as e:
                data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
                return Response(data, status=400)
        else:
            data = {
                    'message': f"Please enter a correct pk. {str(e)}"
                }
            return Response(data, status=400)