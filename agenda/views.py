from django.shortcuts import render, get_object_or_404

from agenda.models import Fotografia

#Responsavel por mostrar o conteudo das telas
def index(request):
    #se eu por um - antes de data_fotografia aparecerá no index a antiga primeiro.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'agenda/index.html',{"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'agenda/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
    return render (request, "agenda/buscar.html", {"cards":fotografias})

def anotacoes(request):
    return render(request, 'agenda/anotacoes.html')


def metas(request):
    return render(request, 'agenda/metas.html')


def tarefas(request):
    return render(request, 'agenda/tarefas.html')


def eventos(request):
    return render(request, 'agenda/eventos.html')