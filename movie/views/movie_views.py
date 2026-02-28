from ..models import Movie
from ..serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class MovieView(APIView):
    def get(self, request, pk=None):
        if pk: #Search just a movie
            try:
                movie = Movie.objects.get(pk=pk)
            except Movie.DoesNotExist:
                return Response({"Error":"Movie not found"}, status=404)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

        querryset = Movie.objects.all() #Request to get all the movies from DB
        serializer = MovieSerializer(querryset, many = True) #Converting model instances into native Python data types (dict/list)
        return Response(serializer.data) #Returning this python object as a JSON file
    

    def post(self, request):
        serializer = MovieSerializer(data=request.data) #Converting JSON in a model instance
        if serializer.is_valid(): #Verifing if is valid
            serializer.save() #Creating or saving
            return Response(serializer.data, status=201) #Everything alright
        return Response(serializer.errors, status=400) #Error
    
    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=404)
        
        serializer = MovieSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"Error":"Movie not found"}, status=404)

        movie.delete()
        return Response(status=204)