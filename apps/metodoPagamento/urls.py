from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'metodoPagamento'

router = routers.DefaultRouter()
router.register('', views.MetodoPagamentoViewSet, basename='metodoPagamento')

urlpatterns = [
    path('', include(router.urls) )
]