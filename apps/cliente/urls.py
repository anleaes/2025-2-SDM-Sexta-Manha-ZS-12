from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cliente'

router = routers.DefaultRouter()
router.register('', views.ClienteViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls) )
]