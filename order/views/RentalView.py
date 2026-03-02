from ..models import RentalModel
from ..serializers import RentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class RentalView(APIView):
    def get(self, request, pk=None):
        if pk: #Search just a movie
            try:
                movie = RentalModel.objects.get(pk=pk)
            except RentalModel.DoesNotExist:
                return Response({"Error":"Movie not found"}, status=404)
            serializer = RentSerializer(movie)
            return Response(serializer.data)

        querryset = RentalModel.objects.all() #Request to get all the movies from DB
        serializer = RentSerializer(querryset, many = True) #Converting model instances into native Python data types (dict/list)
        return Response(serializer.data) #Returning this python object as a JSON file
    
    def post(self, request):
        serializer = RentSerializer(data=request.data) #Converting JSON in a model instance
        if serializer.is_valid(): #Verifing if is valid
            serializer.save() #Creating or saving
            return Response(serializer.data, status=201) #Everything alright
        return Response(serializer.errors, status=400) #Error
    
    def put(self, request, pk):
        try:
            movie = RentalModel.objects.get(pk=pk)
        except RentalModel.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=404)
        
        serializer = RentSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            movie = RentalModel.objects.get(pk=pk)
        except RentalModel.DoesNotExist:
            return Response({"Error":"Movie not found"}, status=404)

        RentalModel.delete()
        return Response(status=204)