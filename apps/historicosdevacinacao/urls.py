from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'historicosdevacinacao'

router = routers.DefaultRouter()
router.register('historicosdevacinacao', views.HistoricoDeVacinacaoViewSet, basename='historicosdevacinacao')

urlpatterns = [
    path('', include(router.urls) )
]