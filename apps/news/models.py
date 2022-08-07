from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

#---------------------||CATEGORIAS
class Categorias(models.Model):
    nombre = models.CharField(max_length=200, null = False)
    
    def __str__ (self):
        return self.nombre


#---------------------||NEWS        
class News (models.Model):
    title = models.CharField(max_length=200, null = False)
    date = models.DateTimeField(auto_now_add = True)
    text = RichTextField(blank=True, null = True)
    active = models.BooleanField(default = True)
    imagen = models.ImageField(upload_to='news', default = 'news/default.png')
    Categorias = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)

    #usuario
    
    def __str__ (self):
        return self.title