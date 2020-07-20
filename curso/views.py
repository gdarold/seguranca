from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm
# Create your views here.

def curso_list(request):
    persons = Curso.objects.all()
    return render(request, 'curso_list.html', {'curso':persons})

def curso_new(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('curso_list')
    return render(request, 'curso_form.html',{'form':form})


def curso_update(request, id):
    disc = get_object_or_404(Curso, pk=id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=disc)
    if form.is_valid():
        form.save()
        return redirect('curso_list')
    return render(request,'Curso_form.html',{'form':form})

def curso_delete(request, id):
    disc = get_object_or_404(Curso, pk=id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=disc)
    if request.method == 'POST':
        disc.delete()
        return redirect('curso_list')
    return render(request, 'curso_confirm_delete.html', {'curso':disc})
