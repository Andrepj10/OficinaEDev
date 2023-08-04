from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Fotografia(models.Model):
    
    
    OPCOES_CATEGORIA = [
        ("BAIXA IMPORTÂNCIA","Baixa importância"),
        ("MODERAMENTE IMPORTANTE","Moderamente importante"),
        ("IMPORTANTE","Importante"),
        ("MUITO IMPORTANTE","Muito importante"),
    ]
    OPCOES_ESTADO = [
        ('Em andamento', 'Em andamento'),
        ('Concluido', 'Concluido'),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_evento = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )
    
    estado = models.CharField(max_length=20, choices=OPCOES_ESTADO, default='Em andamento')
    estado = models.CharField(max_length=20, choices=OPCOES_ESTADO, default='Concluido')

    def __str__(self):
        return self.nome
    
    
    
    