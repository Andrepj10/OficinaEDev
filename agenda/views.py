from django.shortcuts import render, get_object_or_404

from agenda.models import Fotografia

#Responsavel por mostrar o conteudo das telas
def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'agenda/index.html',{"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'agenda/imagem.html', {"fotografia": fotografia})


def anotacoes(request):
    return render(request, 'agenda/anotacoes.html')


def metas(request):
    return render(request, 'agenda/metas.html')


def tarefas(request):
    return render(request, 'agenda/tarefas.html')


def eventos(request):
    return render(request, 'agenda/eventos.html')