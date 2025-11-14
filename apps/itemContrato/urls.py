from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'itemcontrato'

router = routers.DefaultRouter()
router.register('', views.OrderitemViewSet, basename='itens_contrato')

urlpatterns = [
    path('', include(router.urls) )
]