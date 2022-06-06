from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class PlayerPokemon(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pokemon_name = models.CharField(max_length=256)
