from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from agenda.models import Fotografia

#Responsavel por mostrar o conteudo das telas
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'agenda/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'agenda/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
    return render (request, "agenda/buscar.html", {"cards":fotografias})

def anotacoes(request):
     if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
     return render(request, 'agenda/anotacoes.html')


def metas(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    return render(request, 'agenda/metas.html')


def tarefas(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    return render(request, 'agenda/tarefas.html')


def eventos(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    return render(request, 'agenda/eventos.html')