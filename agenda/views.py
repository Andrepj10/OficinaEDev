from django.shortcuts import render

#Responsavel por mostrar o conteudo das telas
def index(request):
    dados = {
        1: {"nome":"Nebulosa de Carina",
            "legenda":"webbtelescope.org / NASA / James Webb"},
        2: {"nome":"Galáxia NGC 1079",
            "legenda":"nasa.org / NASA / Hubble"}
    }
    
    return render(request, 'agenda/index.html',{"cards": dados})

def imagem(request):
    return render(request, 'agenda/imagem.html')