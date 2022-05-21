from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'),    
    path('ver_profissional/<int:id>', views.ver_profissional, name= 'ver_profissional'),
    path('cadastrar_profissional', views.cadastrar_profissional, name= 'cadastrar_profissional'),
    path('excluir_profissional/<int:id>', views.excluir_profissional, name='excluir_profissional')
    
]