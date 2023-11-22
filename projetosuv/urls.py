"""projetosuv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls', namespace='pacientes')),
    path('postodesaude/', include('postodesaude.urls', namespace='postodesaude')),
    path('agendamentos/',include('agendamentos.urls', namespace='agendamentos')),
    path('vacinas/',include('vacinas.urls', namespace='vacinas')),
    path('lotes_de_vacina/', include('vacinas.urls', namespace='lotes_de_vacinas')),
    path('atendente/',include('atendentes.urls',namespace='atendentes')),
    path('historicodevacinacao/',include('historicosdevacinacao.urls',namespace='historicosdevacinacao'))
]
