from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Profissional
from usuarios.models import Usuario 
from .forms import CadastroProfissional 




def home(request): 
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        profissional = Profissional.objects.all()
        form = CadastroProfissional()
        return render(request, 'home.html', {'profissional': profissional, 'usuario_logado':
                                                 request.session.get('usuario'),
                                                 'form': form})
    else:
        return redirect('/auth/login/?status=2') 


def ver_profissional(request, id):
    profissional = Profissional.objects.get(id = id)
    return render(request, 'ver_profissional.html', {'profissional' : profissional, 'usuario_logado': request.session.get('usuario')} )

def cadastrar_profissional(request):
    if request.method == 'POST':
        form = CadastroProfissional(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('salvo')
        else:
            return HttpResponse('errado')    