from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'fornecedor'

router = routers.DefaultRouter()
router.register('', views.FornecedorViewSet, basename='fornecedores')

urlpatterns = [
    path('', include(router.urls) )
]