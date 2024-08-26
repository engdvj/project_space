from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),  # Corrigido 'nome' para 'name'
    path('imagem/', imagem, name='imagem')  # Corrigido 'nome' para 'name'
]
