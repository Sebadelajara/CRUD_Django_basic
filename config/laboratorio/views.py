from django.shortcuts import render, redirect
from .models import Laboratorio
# Create your views here.

def lab(request):
    laboratorio = Laboratorio.objects.all().order_by('nombre')
    return render(request, 'lab.html', {'laboratorio': laboratorio})

def formadd(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']

        Laboratorio.objects.create(nombre=nombre, ciudad=ciudad, pais=pais)
        return redirect('/lab')
    else:
        return render(request, 'lab.html')



def editar(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
   
    return render(request, 'editar.html', {'laboratorio': laboratorio})

def editarlab(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']
    new_lab = Laboratorio.objects.get(id=id)
    new_lab.nombre = nombre
    new_lab.ciudad = ciudad
    new_lab.pais = pais
    new_lab.save()
    return redirect('/lab')

def eliminar(request, id):
    lab_delete = Laboratorio.objects.get(id=id)
    lab_delete.delete()
    return redirect('/lab')



