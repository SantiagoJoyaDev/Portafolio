from django.shortcuts import render

def home(request):
    return render(request, "portfolio/home.html")
        
def sobre_mi(request):
    return render(request, "portfolio/sobre_mi.html")
