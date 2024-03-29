"""poke_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from pokemon.views import *

# pokemon_router = routers.DefaultRouter()
# pokemon_router.register('allpokemon', PokemonViewSet);

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemon/allpokemon/', AllPokemonViewSet.as_view({'get':'list'})),
    path('pokemon/uncapturedpokemon/', uncaptured_pokemon),
    path('pokemon/capturedpokemon/', add_or_view),
    path('pokemon/releasepokemon/', release_pokemon),
    path('pokemon/wildpokemon/', WildPokemonViewSet.as_view({'get':'list'})),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
]
