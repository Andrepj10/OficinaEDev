from django.urls import path
from apps.agenda.views import index, imagem, buscar
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
    path('anotacoes/', views.anotacoes, name='anotacoes'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('metas/', views.metas, name='metas'),
    path('eventos/', views.eventos, name='eventos'),



    
]