from django.urls import path
from apps.agenda.views import index, imagem, buscar

from apps.agenda.views import novo_evento, editar_evento, deletar_evento, filtro, evento_andamento, evento_concluido, concluir_evento

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
    path('anotacoes/', views.anotacoes, name='anotacoes'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('metas/', views.metas, name='metas'),
    
    
    
    path('eventos/', views.eventos, name='eventos'),
    path('novo-evento', novo_evento, name='novo_evento'),
    path('editar-evento/<int:foto_id>', editar_evento, name='editar_evento'),
    path('deletar-evento/<int:foto_id>', deletar_evento, name='deletar_evento'),
    path('concluir-evento/<int:foto_id>', concluir_evento, name='concluir_evento'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
    
    path('evento-andamento', evento_andamento, name='evento_andamento'),
    path('evento-concluido', evento_concluido, name='evento_concluido'),


    
]