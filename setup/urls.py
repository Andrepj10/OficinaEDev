
from django.contrib import admin
from django.urls import path
from agenda.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]
