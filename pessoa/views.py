from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.views.generic.base import View

from seguranca.models import Login
from .models import Person
from .forms import PersonForm
# Create your views here.

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons':persons})

def personsAluno_list(request):
    persons = Person.objects.all()
    return render(request, 'personAluno_list.html', {'persons':persons})

def personsProfessor_list(request):
    persons = Person.objects.all()
    return render(request, 'personProfessor_list.html', {'persons':persons})

def persons_new(request):

    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        person = form.save(commit=False)
        logis = Login.objects.get(nome=person.user)
        logis.permissions = str(person.funcao)
        logis.save()
        person.save()



        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})



def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request,'person_form.html',{'form':form})

def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_confirm_delete.html', {'person':person})
