from django.shortcuts import render
from .models import Libro
# Create your views here.
def lista_libros(request):
  libros=Libro.objects.all()
  return render(request,'lista_libros.html',{'libros':libros})
  