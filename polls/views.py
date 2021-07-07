from django.shortcuts import render

# Create your views here.
def Pagina_Inicial(request):
    return render(request, 'Pagina_Inicial.html')
