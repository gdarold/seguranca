from django.contrib import admin
from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete





urlpatterns = [

    path('list/',persons_list, name="person_list"),
    path('new/', persons_new, name="person_create"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/',persons_delete, name="persons_delete"),

    ]