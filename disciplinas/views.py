from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Disciplina
from .forms import DisciplinaForm
# Create your views here.

def disciplinas_list(request):
    persons = Disciplina.objects.all()
    return render(request, 'disciplinas_list.html', {'disciplinas':persons})

def disciplinas_new(request):
    form = DisciplinaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('disciplinas_list')
    return render(request, 'disciplinas_form.html',{'form':form})


def disciplinas_update(request, id):
    disc = get_object_or_404(Disciplina, pk=id)
    form = DisciplinaForm(request.POST or None, request.FILES or None, instance=disc)
    if form.is_valid():
        form.save()
        return redirect('disciplinas_list')
    return render(request,'disciplinas_form.html',{'form':form})

def disciplinas_delete(request, id):
    disc = get_object_or_404(Disciplina, pk=id)
    form = DisciplinaForm(request.POST or None, request.FILES or None, instance=disc)
    if request.method == 'POST':
        disc.delete()
        return redirect('disciplinas_list')
    return render(request, 'disciplinas_confirm_delete.html', {'disciplina':disc})
