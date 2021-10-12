from django.db import models


class Formulario(models.Model):
    pk_ID = models.AutoField(primary_key=True, null=False, blank=False)
    Nombre = models.CharField(max_length=50, null=False, blank=False)
    Correo = models.CharField(max_length=50, null=False, blank=False)
    Direccion = models.TextField(max_length=100, null=False, blank=False)
    msj = models.DecimalField(null=False, max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'
        ordering = ['Nombre']

    def __str__(self):
        return "{0}".format(self.Nombre)

# Create your models here.
