from django.urls import path
from . import views
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

urlpatterns = [
    path('games/', views.game_list, name='game-list'),
    path('games/<int:pk>/', views.game_detail, name='game-detail'),
]
@csrf_exempt
def game_list(request):
    if request.method == 'GET':
        # lógica para obter todos os jogos e retornar como JSON
        pass
    elif request.method == 'POST':
        data = json.loads(request.body)
        # lógica para adicionar um novo jogo com os dados fornecidos
        pass

@csrf_exempt
def game_detail(request, pk):
    if request.method == 'GET':
        # lógica para obter um jogo específico com o id fornecido e retornar como JSON
        pass
