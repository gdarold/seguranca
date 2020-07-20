from django.contrib import admin
from django.urls import path
from .views import persons_list, personsAluno_list, personsProfessor_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete






urlpatterns = [

    path('list/',persons_list, name="person_list"),
    path('listAluno/',personsAluno_list, name="personAluno_list"),
    path('listProfessor/',personsProfessor_list, name="personProfessor_list"),


    path('new/', persons_new, name="person_create"),

    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/',persons_delete, name="persons_delete"),

    ]