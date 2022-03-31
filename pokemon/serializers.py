from pokemon.models import Pokemon
from rest_framework import serializers


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name']

class PokemonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'hp', 'attack', 'defense', 'type', 'level']