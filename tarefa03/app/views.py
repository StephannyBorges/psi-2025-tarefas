from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def usuarios(request):
    lista_usuarios = [
        {"nome": "Matheus","matricula":12345, "idade": 19, "cidade": "São Paulo"},
        {"nome": "Ana","matricula":98763, "idade": 21, "cidade": "São Tomé"},
        {"nome": "Erika","matricula":98234, "idade": 17, "cidade": "Bahia"},
        {"nome": "Joyce","matricula":65349, "idade": 23, "cidade": "Barcelona"},
        {"nome": "Beatriz","matricula":98006, "idade": 20, "cidade": "São Pedro"},
       
    ]

    context = {
        "usuarios": lista_usuarios,
    }
    return render(request, "usuarios.html", context)
