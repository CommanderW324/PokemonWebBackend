from django.http import Http404
from django.shortcuts import render

# Create your views here.
from pokemon.models import Pokemon
from pokemon.serializers import *

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def add_or_view(request):
    user = request.user
    if request.method == 'POST':
        new_captured_pokemon = Pokemon.objects.get(id=int(request.data['id']))
        new_captured_pokemon.trainer = user
        new_captured_pokemon.save(update_fields=['trainer'])
        serialize = PokemonDetailSerializer(new_captured_pokemon)
        return Response(serialize.data)
    
    try:
        captured_pokemon = Pokemon.objects.filter(trainer=user)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PokemonDetailSerializer(captured_pokemon, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def release_pokemon(request):
    released_pokemon_id = int(request.data['id'])
    try:
        released_pokemon = Pokemon.objects.get(id=released_pokemon_id)
        released_pokemon.trainer= None
        released_pokemon.save(update_fields=['trainer'])
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_200_OK)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def uncaptured_pokemon(request):
    user = request.user
    print(user)
    try:
        uncaptured_pokemon = Pokemon.objects.exclude(trainer=user)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PokemonSerializer(uncaptured_pokemon, many=True)
    return Response(serializer.data)
    



class AllPokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class WildPokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.filter(trainer=None)
    serializer_class = PokemonSerializer    
