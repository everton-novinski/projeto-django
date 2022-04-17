from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('inserir/', views.inserir, name = 'inserir'),
    path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('valida_login/', views.valida_login, name = 'valida_login'),
    path('sair/', views.sair, name='sair')
    
] 