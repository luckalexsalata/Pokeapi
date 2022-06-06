from rest_framework import serializers
from api.models import Player, PlayerPokemon


class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class PlayerPokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerPokemon
        fields = [
            'player',
            'pokemon_name',
        ]





