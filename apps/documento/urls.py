from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'documentos'

router = routers.DefaultRouter()
router.register('', views.DocumentoViewSet, basename='documentos')

urlpatterns = [
    path('', include(router.urls) )
]