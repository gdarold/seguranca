"""segurancaInfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from seguranca import urls as seguranca_urls
from pessoa import urls as pessoas_urls
from notas import urls as notas_urls
from curso import urls as curso_urls

from disciplinas import urls as disciplinas_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(seguranca_urls)),
    path('pessoa/', include(pessoas_urls)),
    path('notas/', include(notas_urls)),
    path('disciplinas/', include(disciplinas_urls)),
    path('curso/', include(curso_urls)),


]
