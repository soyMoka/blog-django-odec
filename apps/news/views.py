import imp
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import News, Categorias
# Create your views here.


################# ||Agragar Post ############################## 

class addNews(CreateView):
    model=News
    fields = ['title', 'text', 'Categorias', 'imagen']
    template_name = 'news/addNews.html'
    success_url = reverse_lazy('index')

#-----------END---END---END---END---END---END---END------------

################# ||Mostrar Posts #############################

class mostrarNews(ListView):
    model = News
    template_name: str = 'news/listarNews.html'

#-----------END---END---END---END---END---END---END------------  


def ListarNews(request):
    noticia = News
    context = {
        'noticia': noticia
    }
    return render(request, 'news/listarNews2.html', context)

def listarNewsPorCaregorias(request, categoria):
    categoria2 = Categorias.objects.filter(nombre = Categorias)

    noticia = News.objects.filter(categorias = categoria2[0].id)
    context = {
        'noticia': noticia
    }
    return render(request, 'noticia/listarNews2.html', context)