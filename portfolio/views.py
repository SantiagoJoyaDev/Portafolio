from django.shortcuts import render

def home(request):
    return render(request, "portfolio/home.html")
        
def sobre_mi(request):
    return render(request, "portfolio/sobre_mi.html")

def proyectos(request):
    return render(request, "portfolio/proyectos.html")

def habilidades(request):
    return render(request, "portfolio/habilidades.html")

def contacto(request):
    return render(request, "portfolio/contacto.html")