from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'),    
    path('ver_profissional/<int:id>', views.ver_profissional, name= 'ver_profissional')
    
]