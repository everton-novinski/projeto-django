from django.contrib import admin
from .models import Avaliacao, Profissional, Especialidades


admin.site.register(Profissional)
admin.site.register(Especialidades)
admin.site.register(Avaliacao)

