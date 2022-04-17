from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Profissional
from usuarios.models import Usuario   




def home(request): 
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        profissional = Profissional.objects.all()
        return render(request, 'home.html', {'profissional': profissional})
    else:
        return redirect('/auth/login/?status=2') 


def ver_profissional(request, id):
    profissional = Profissional.objects.get(id = id)
    return render(request, 'ver_profissional.html', {'profissional' : profissional} )
