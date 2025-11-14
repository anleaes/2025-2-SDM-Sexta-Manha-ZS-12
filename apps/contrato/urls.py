from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'contratos'

router = routers.DefaultRouter()
router.register('', views.ContratoViewSet, basename='pedidos')

urlpatterns = [
    path('', include(router.urls) )
]