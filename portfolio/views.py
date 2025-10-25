from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a mi portafolio</h1><p>Este es mi primer proyecto con Django.</p>")
