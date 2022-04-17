
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicial),
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),
    path('auth/', include ('usuarios.urls')),
    
]
