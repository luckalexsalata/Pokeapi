from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(User)
admin.site.register(Player)
admin.site.register(PlayerPokemon)