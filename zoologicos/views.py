from rest_framework import viewsets
from .models import Zoologico, Especie, Familia
from .serializers import (
    ZoologicoSerializer, 
    EspecieSerializer, 
    FamiliaSerializer, 
    ZooCrearActualizarSerializer
)

class ZoologicoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de los Zoológicos.
    Usa un serializador diferente para la creación/actualización.
    """
    queryset = Zoologico.objects.all()

    def get_serializer_class(self):
        # Usa el serializador especializado para las acciones de creación y actualización
        if self.action in ['create', 'update', 'partial_update']:
            return ZooCrearActualizarSerializer
        # Para el resto de las acciones (listado, detalle), usa el serializador por defecto
        return ZoologicoSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
