from django.urls import path
from .views import TituloLista, TituloDetalle, TituloFecha, TituloBaja, TituloPagoCuota

urlpatterns = [
    path('titulo-bancario/', TituloLista.as_view(), name='titulo_lista'),
    path('titulo-bancario/<int:pk>/', TituloDetalle.as_view(), name='titulo_detalle'),
    path( 'titulo-bancario/fecha/', TituloFecha.as_view(), name='titulo_fecha'),
    path( 'titulo-bancario/baja/<str:idtitulo>/', TituloBaja.as_view(), name='titulo_baja'),
    path( 'titulo-bancario/pagocuota/', TituloPagoCuota.as_view(), name='titulo_pagocuota'),
]
