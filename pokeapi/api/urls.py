from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
import api.views as api_views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("create-player", api_views.PlayerCreateView.as_view()),
    path("player/<int:pk>", api_views.PlayerDetailView.as_view(), name="player"),
    path('home/', api_views.PlayerHomeView.as_view(), name='home'),
    path('delete-pokemon/<int:pk>/', api_views.PlayerPokemonDestroyView.as_view()),
    path('list-player/', api_views.PlayerListViev.as_view(), name='list-player')
]