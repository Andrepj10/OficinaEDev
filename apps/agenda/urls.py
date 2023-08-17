from django.urls import path

from apps.agenda.views import index, imagem, buscar

from apps.agenda.views import novo_evento, editar_evento, deletar_evento\
    ,filtro, evento_andamento, evento_concluido \
        ,concluir_evento, nova_meta, editar_meta, deletar_meta\
            ,concluir_meta, meta_andamento, meta_concluida\
                ,nova_anotacao, editar_anotacao, deletar_anotacao, anotacao_andamento\
                    ,nova_tarefa, editar_tarefa, deletar_tarefa, concluir_tarefa, tarefa_andamento, tarefa_concluida\


from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
  
    path('anotacoes/', views.anotacoes, name='anotacoes'),
    path('nova-anotacao', nova_anotacao, name='nova_anotacao'),
    path('editar-anotacao/<int:anotacao_id>/', editar_anotacao, name='editar_anotacao'),
    path('deletar-anotacao/<int:anotacao_id>', deletar_anotacao, name='deletar_anotacao'),
    path('anotacao-andamento', anotacao_andamento, name='anotacao_andamento'),
    
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

    path('tarefas/', views.tarefas, name='tarefas'),
    path('nova-tarefa', nova_tarefa, name='nova_tarefa'),
    path('editar-tarefa/<int:tarefa_id>/', editar_tarefa, name='editar_tarefa'),
    path('deletar-tarefa/<int:tarefa_id>', deletar_tarefa, name='deletar_tarefa'),
    path('concluir-tarefa/<int:tarefa_id>', concluir_tarefa, name='concluir_tarefa'),
    path('tarefa-andamento', tarefa_andamento, name='tarefa_andamento'),
    path('tarefa-concluida', tarefa_concluida, name='tarefa_concluida'),

    
]