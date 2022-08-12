from django.urls import path

from . import views
app_name = 'apps.news'

urlpatterns = [
    path('addNews/', views.addNews.as_view(), name='news_add'),
    path('listarNews/', views.mostrarNews.as_view(), name='news_list'),
    path('detail/<int:pk>', views.newsDetailView.as_view (), name= 'news_detail'),
    path('editNews/<int:pk>', views.editNews.as_view(), name='news_edit'),

    #path('readnew/<int:id>', views.ReadNew, name="readnew"),
    #path('listarNews2/', views.ListarNews()),
    #path('listarCategoria/<str:categoria>', views.ListarNewsPorCategoria, name='listarCategoria'),
    
     
]