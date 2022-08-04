from django.urls import path

from . import views
app_name = 'apps.news'

urlpatterns = [
    path('addNews/', views.addNews.as_view()),
    #path('listarNews/', views.mostrarNews.as_view()),
    #path('listarNews2/', views.ListarNews()),
    #path('listarCategoria/<str:categoria>', views.ListarNewsPorCategoria, name='listarCategoria'),
    
     
]