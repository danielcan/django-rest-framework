"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from tiendas.views import TiendaList, TiendaDetail
from marcas_api.views import MarcasList, MarcasDetail
from ofertas.views import OfertasList, OfertasDetail
from favorito.views import FavoritoList, FavoritoDetail

urlpatterns = [
    path('api/user', FavoritoList.as_view()),
    path('api/deals', OfertasList.as_view()),
    path('api/brands', MarcasList.as_view()),
    path('api/stores', TiendaList.as_view()),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
