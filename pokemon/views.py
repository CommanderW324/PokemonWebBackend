from django.http import Http404
from django.shortcuts import render

# Create your views here.
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from rest_framework import viewsets, APIView, permissions, status
from rest_framework.response import Response
class PokemonUserView(APIView):
    """
    Retrieve, update or delete a Pokemon instance.
    """
    def get_object(self, id):
        try:
            return Pokemon.objects.get(id = id)
        except Pokemon.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Pokemon = self.get_object(id)
        serializer = PokemonSerializer(Pokemon)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Pokemon = self.get_object(id)
        serializer = PokemonSerializer(Pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Pokemon = self.get_object(id)
        Pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticated]