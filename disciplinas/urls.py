from django.urls import path

from curso.views import curso_list, curso_delete, curso_new, curso_update

urlpatterns = [

    path('list/',curso_list, name="curso_list"),
    path('new/', curso_new, name="curso_create"),
    path('update/<int:id>/', curso_update, name="curso_update"),
    path('delete/<int:id>/',curso_delete, name="curso_delete"),

    ]