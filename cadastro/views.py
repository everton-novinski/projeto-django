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
        form.fields['usuario'].initial = request.session['usuario']

        return render(request, 'home.html', {'profissional': profissional, 'usuario_logado':
                                                 request.session.get('usuario'),
                                                 'form': form})
    else:
        return redirect('/auth/login/?status=2') 


def ver_profissional(request, id):
    profissional = Profissional.objects.get(id = id)
    form = CadastroProfissional()
    usuario = Usuario.objects.get(id = request.session['usuario'])
    form.fields['usuario'].initial = request.session['usuario']
    
    return render(request, 'ver_profissional.html', {'profissional' : profissional, 
                                                    'usuario_logado': request.session.get('usuario'),
                                                    'form' : form,
                                                    'id_profissional': id,} )

def cadastrar_profissional(request):
    if request.method == 'POST':        
        form = CadastroProfissional(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('errado') 

def excluir_profissional(request, id):
    usuario = Usuario.objects.get(id = request.session['usuario'])
    profissional = Profissional.objects.get(id = id).delete()
    return redirect('/cadastro/home')
