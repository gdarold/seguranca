from django.urls import path

from notas.views import notas_list, notas_new, notas_update, notas_delete

urlpatterns = [

    path('list/',notas_list, name="notas_list"),
    path('new/', notas_new, name="notas_create"),
    path('update/<int:id>/', notas_update, name="notas_update"),
    path('delete/<int:id>/',notas_delete, name="notas_delete"),

    ]