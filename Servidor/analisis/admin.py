from django.contrib import admin
from .models import Datos_pacientes, Antecedentes_pacientes, Informacion_medica

admin.site.register(Datos_pacientes)
admin.site.register(Antecedentes_pacientes)
admin.site.register(Informacion_medica)
