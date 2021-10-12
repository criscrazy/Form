from django.shortcuts import render
from django.shortcuts import render
from .models import *


def index(request):
    allForm = Formulario.objects.all()
    return render(request, 'index.html')

# Create your views here.
