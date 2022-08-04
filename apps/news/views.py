import imp
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import News, Categorias
# Create your views here.

class addNews(CreateView):
    model=News
    fields = ['title', 'text', 'Categorias', 'imagen']
    template_name = 'news/addNews.html'
    success_url = reverse_lazy('index')

class mostrarNews(ListView):
    model = News
    template_name: str = 'news/listarNews.html'
    
def ListarNews(request):
    noticia = News
    context = {
        'noticia': noticia
    }
    return render(request, 'news/listarNews2.html', context)

