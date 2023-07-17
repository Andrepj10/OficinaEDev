from django.shortcuts import render

#Responsavel por mostrar o conteudo das telas

def index(request):
    return render(request, 'agenda/index.html')

def imagem(request):
    return render(request, 'agenda/imagem.html')