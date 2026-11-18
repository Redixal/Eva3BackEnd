from django.urls import path
from .views import (
    VideojuegoListView, VideojuegoDetailView,
    VideojuegoCreateView, VideojuegoUpdateView, VideojuegoDeleteView
)

urlpatterns = [
    path('', VideojuegoListView.as_view(), name='videojuego_list'),
    path('detalle/<int:pk>/', VideojuegoDetailView.as_view(), name='videojuego_detail'),
    path('nuevo/', VideojuegoCreateView.as_view(), name='videojuego_create'),
    path('editar/<int:pk>/', VideojuegoUpdateView.as_view(), name='videojuego_update'),
    path('eliminar/<int:pk>/', VideojuegoDeleteView.as_view(), name='videojuego_delete'),
]