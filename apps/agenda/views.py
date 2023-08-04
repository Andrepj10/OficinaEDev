from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from apps.agenda.models import Fotografia
from apps.agenda.forms import FotografiaForms
from datetime import datetime
from django.db.models import Q

#Responsavel por mostrar o conteudo das telas
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_evento").filter(publicada=True)
    return render(request, 'agenda/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'agenda/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_evento").filter(publicada=True)
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
    return render (request, "agenda/index.html", {"cards":fotografias})

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


def novo_evento(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo evento cadastrado ')
            return redirect('index')
            
    return render(request, 'agenda/novo_evento.html', {'form': form})

def editar_evento(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, 'Evento editado com sucesso')
            return redirect('index')
    
    return render(request, 'agenda/editar_evento.html', {'form':form, 'foto_id': foto_id})




def deletar_evento(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')




def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_evento").filter(publicada=True, categoria=categoria)

    return render(request, 'agenda/index.html', {"cards": fotografias})


def evento_andamento(request):
    # Filtra as fotografias em andamento com base no campo "estado"
    fotografias = Fotografia.objects.filter(estado='Em andamento', publicada=True)

    # Renderiza a lista de fotografias em andamento no template eventos_andamento.html
    return render(request, 'agenda/evento_andamento.html', {'cards': fotografias})




def concluir_evento(request,foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.estado = 'Concluido'
    fotografia.save()
    messages.success(request, 'Conclusão feita com sucesso!')
    return redirect('index')


def evento_concluido(request):
    # Filtra as fotografias em andamento com base no campo "estado"
    fotografias = Fotografia.objects.filter(estado='Concluido')


    return render(request, 'agenda/evento_concluido.html', {'cards': fotografias})

