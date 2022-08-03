from django.db import models
from apps.news.models import News

# Create your models here.


class Comentarios(models.Model):
    coment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #user = (aún no creamos la app user, por lo que no lo podemos usar aún)
    noticia = models.ForeignKey(News, on_delete=models.CASCADE) # el models.CASCADE hace que si se elimina la noticia el comentario tambien lo hace.
    