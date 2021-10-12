from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class resourceFormulario(resources.ModelResource):
    class Meta:
        model = Formulario


class AdminFormulario(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ['Correo', 'Direccion', 'msj']
    resource_class = resourceFormulario


admin.site.register(Formulario, AdminFormulario)
# Register your models here.
