from ..models import Customer
from ..serializers import CustomerSerialiizer
from rest_framework.views import APIView
from rest_framework.response import Response

class CustomerView(APIView):
    def get(self, request, pk=None):
        if pk: #Search just a movie
            try:
                movie = Customer.objects.get(pk=pk)
            except Customer.DoesNotExist:
                return Response({"Error":"Movie not found"}, status=404)
            serializer = CustomerSerialiizer(movie)
            return Response(serializer.data)

        querryset = Customer.objects.all() #Request to get all the movies from DB
        serializer = CustomerSerialiizer(querryset, many = True) #Converting model instances into native Python data types (dict/list)
        return Response(serializer.data) #Returning this python object as a JSON file
    
    def post(self, request):
        serializer = CustomerSerialiizer(data=request.data) #Converting JSON in a model instance
        if serializer.is_valid(): #Verifing if is valid
            serializer.save() #Creating or saving
            return Response(serializer.data, status=201) #Everything alright
        return Response(serializer.errors, status=400) #Error
    
    def put(self, request, pk):
        try:
            movie = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"Error": "Movie not found"}, status=404)
        
        serializer = CustomerSerialiizer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            movie = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({"Error":"Movie not found"}, status=404)

        movie.delete()
        return Response(status=204)