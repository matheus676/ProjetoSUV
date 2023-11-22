from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'atendentes'

router =  routers.DefaultRouter()
router.register('atendentes',views.AtendenteViewSet,basename='Atendentes')

urlpatterns = [
  path('',include(router.urls))

]
