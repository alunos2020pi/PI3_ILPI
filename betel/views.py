from django.shortcuts import render

# Create your views here.
def index(request):
    '''Função view para a página index'''
    return render(request, 'index.html')
