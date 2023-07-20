from django.urls import path
from agenda.views import index, imagem, anotacoes
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('anotacoes/', views.anotacoes, name='anotacoes'),

    
]