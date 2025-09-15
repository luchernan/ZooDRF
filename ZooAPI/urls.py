from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from zoologicos.views import ZoologicoViewSet, EspecieViewSet, FamiliaViewSet

# Router de DRF para generar automáticamente las rutas CRUD

router = DefaultRouter()
router.register(r'zoologicos', ZoologicoViewSet, basename='zoologico')
router.register(r'especies', EspecieViewSet, basename='especie')
router.register(r'familias', FamiliaViewSet, basename='familia')

urlpatterns = [
    path('admin/', admin.site.urls),        # Sitio administrativo de Django
    path('api/', include(router.urls)),     # Endpoints de la API (REST)
]
