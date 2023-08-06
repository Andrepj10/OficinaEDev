from django.urls import path

from apps.agenda.views import index, imagem, buscar

from apps.agenda.views import novo_evento, editar_evento, deletar_evento\
    ,filtro, evento_andamento, evento_concluido \
        ,concluir_evento, nova_meta, editar_meta, deletar_meta, concluir_meta, meta_andamento, meta_concluida

from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
    path('anotacoes/', views.anotacoes, name='anotacoes'),
    path('tarefas/', views.tarefas, name='tarefas'),
    
    path('metas/', views.metas, name='metas'),
    path('nova-meta', nova_meta, name='nova_meta'),
    path('editar-meta/<int:meta_id>/', editar_meta, name='editar_meta'),
    path('deletar-meta/<int:meta_id>', deletar_meta, name='deletar_meta'),
    path('concluir-meta/<int:meta_id>', concluir_meta, name='concluir_meta'),
    
    path('meta-andamento', meta_andamento, name='meta_andamento'),
    path('meta-concluida', meta_concluida, name='meta_concluida'),


    
    
    
    path('eventos/', views.eventos, name='eventos'),
    path('novo-evento', novo_evento, name='novo_evento'),
    path('editar-evento/<int:foto_id>', editar_evento, name='editar_evento'),
    path('deletar-evento/<int:foto_id>', deletar_evento, name='deletar_evento'),
    path('concluir-evento/<int:foto_id>', concluir_evento, name='concluir_evento'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
    
    path('evento-andamento', evento_andamento, name='evento_andamento'),
    path('evento-concluido', evento_concluido, name='evento_concluido'),


    
]