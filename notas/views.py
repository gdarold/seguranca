from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notas
from .forms import NotasForm
# Create your views here.

def notas_list(request):
    persons = Notas.objects.all()
    return render(request, 'notas_list.html', {'notas':persons})

def notas_new(request):
    form = NotasForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('notas_list')
    return render(request, 'notas_form.html',{'form':form})


def notas_update(request, id):
    person = get_object_or_404(Notas, pk=id)
    form = NotasForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('notas_list')
    return render(request,'notas_form.html',{'form':form})

def notas_delete(request, id):
    nota = get_object_or_404(Notas, pk=id)
    form = NotasForm(request.POST or None, request.FILES or None, instance=nota)
    if request.method == 'POST':
        nota.delete()
        return redirect('notas_list')
    return render(request, 'notas_confirm_delete.html', {'nota':nota})
