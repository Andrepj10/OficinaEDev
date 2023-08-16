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
    

    def __str__(self):
        return self.nome
    

class FazerMeta(models.Model):
    
    OPCOES_MODO = [
        ('Meta em andamento', 'Meta em andamento'),
        ('Meta Concluida', 'Meta Concluida'),
    ]
    
    nomeMeta = models.CharField(max_length=100, null=False, blank=False)
    data_inicio = models.DateField(null=False, blank=False)
    data_fim = models.DateField(null=False, blank=False)
    quantidade_passos = models.IntegerField(null=False, blank=False)

    modo = models.CharField(max_length=20, choices=OPCOES_MODO, default='Meta em andamento')
    
    def __str__(self):
        return self.nomeMeta
    
    
    
class FazerAnotacao(models.Model):
    
    nomeAnotacao = models.CharField(max_length=1000)
    descricao = models.TextField()  # Adicionando o campo descrição
    

    def __str__(self):
        return self.nomeAnotacao