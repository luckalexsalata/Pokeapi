from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests


class PlayerCreateView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlayerHomeView(generics.CreateAPIView):
    serializer_class = PlayerPokemonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        player = Player.objects.get(user=request.user)
        pokemons_count = PlayerPokemon.objects.filter(player=player).count()
        return Response({
            "username": request.user.username,
            "pokemons_count": pokemons_count,
        })

    def post(self, request, *args, **kwargs):
        pokemon_name = self.request.data['pokemon_name']
        r = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemon_name)
        player = Player.objects.get(user=request.user)
        if r:
            if PlayerPokemon.objects.filter(player=player, pokemon_name=pokemon_name).exists():
                return Response({
                    "error": 'you already added this pokemon',
                })
            else:
                pokemon = PlayerPokemon(player=player, pokemon_name=pokemon_name)
                pokemon.save()
                return Response({
                    "saved": pokemon_name,
                })
        else:
            return Response({
                "error": 'not found this pokemon',
            })


class PlayerPokemonDestroyView(generics.DestroyAPIView):
    queryset = PlayerPokemon.objects.all()
    serializer_class = PlayerPokemonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlayerListViev(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        gamers = Player.objects.all()
        data = []
        for gamer in gamers:
            pokemons = PlayerPokemon.objects.filter(player=gamer).values('pokemon_name')

            player_data = {
                'player': gamer.user.username,
                'pokemons': list(pokemons)
            }
            data.append(player_data)
        return Response({
            'player_list':data
        })

