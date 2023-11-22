from django.urls import path, include
from .import views
from rest_framework import routers

app_name = 'Vacinas'

router = routers.DefaultRouter()
router.register('vacinas', views.VacinaViewSet, basename='vacinas')
router.register('lotes_de_vacinas', views.LoteDeVacinaViewSet, basename='lotes_de_vacinas')
urlpatterns = [
    path('', include(router.urls) )
]