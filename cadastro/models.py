from django.db import models
from datetime import date
from usuarios.models import Usuario


class Especialidades(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Especialidade'

    def __str__(self):
        return self.nome  

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    data_cadastro = models.DateField(default= date.today)
    descricao = models.TextField()
    especialidades = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Profissional'

    def __str__(self):
        return self.nome   

class Avaliacao(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    nome_avaliador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True) 
    
    class Meta:
        verbose_name = 'Avaliaçao'

    def __str__(self) -> str:
        return self.avaliacao    
