from django.urls import path

from disciplinas.views import disciplinas_new, disciplinas_update, disciplinas_list, disciplinas_delete, \
    disciplinasProfessor_list

urlpatterns = [

    path('list/',disciplinas_list, name="disciplinas_list"),
    path('profelist/',disciplinasProfessor_list, name="disciplinasProfessor_list"),

    path('new/', disciplinas_new, name="disciplinas_create"),
    path('update/<int:id>/', disciplinas_update, name="disciplinas_update"),
    path('delete/<int:id>/',disciplinas_delete, name="disciplinas_delete"),

    ]