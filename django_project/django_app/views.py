from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}
	return render(request, 'django/index.html', dicionario_contexto)

def sobre(request):
	return render(request, 'django/sobre.html', {'opa': 'apenas teste'})
