from django.http import Http404
from django.shortcuts import render

# Create your views here.
from pokemon.models import Pokemon
from pokemon.serializers import *

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def add_or_view(request):
    print(request)
    user = request.user
    if request.method == 'POST':
        pokemon_detail = Pokemon.objects.get(id=request.data['id'])
        print(pokemon_detail)
        serializer = PokemonDetailSerializer(Pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        captured_pokemon = Pokemon.objects.filter(trainer=user)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PokemonSerializer(captured_pokemon, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def release_pokemon(request):
    released_pokemon_id = request.data['id']
    try:
        released_pokemon = Pokemon.objects.get(id=released_pokemon_id)
        released_pokemon.trainer= None
        released_pokemon.save(update_fields=['trainer'])
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)
    

@api_view(['GET'])
def uncaptured_pokemon(request):
    user = request.user
    print(user)
    try:
        uncaptured_pokemon = Pokemon.objects.exclude(trainer=user)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PokemonSerializer(uncaptured_pokemon, many=True)
    return Response(serializer.data)
    



class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticated]