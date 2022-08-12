
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,  CreateView, UpdateView
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

class editNews(UpdateView):
    model = News
    template_name = 'news/editNews.html'
    fields = ['title', 'text','imagen', 'Categorias' ]


############## ||Detalle Post ##################

class newsDetailView(DetailView):
    model = News
    template_name = 'news/detailNews.html'


#-----------END---END---END---END---END---END---END-----------


###############| ReadPost de Augusto |#########################

def ReadPost(request, id):
	try:
		posts = ExistePost(id)
	except Exception:
		posts = Post.objects.get(id=id)
	comentarios = Comentario.objects.filter(post=id)

	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated:
			aux =  form.save(commit=False)
			aux.post = posts
			aux.user = request.user
			aux.save()
			form = ComentarioForm()
		else:
			return redirect('usuario:login')
	
	context = {
		'titulo': 'post',
		'posts': posts,
		'form': form,
		'comentarios': comentarios
	}
	return render(request,'post/post.html', context)


def ExistePost(id):
	for i in cache.get('posts'):
		if i.id == id:
			return i
	return None


#######################################

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
    return render(request, 'noticia/listarNews2.html',)