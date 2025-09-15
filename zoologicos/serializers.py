from rest_framework import serializers
from .models import Familia, Especie, Zoologico as Zoo
from django.db import transaction
from collections import defaultdict


# Serializer para el modelo Familia 
class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = ['id', 'nombre']


# Serializer para Especie: incluye familia en modo lectura y familia_id en modo escritura
class EspecieSerializer(serializers.ModelSerializer):
    # Muestra los datos completos de la familia en la respuesta
    familia = FamiliaSerializer(read_only=True)
    # Permite asignar familia enviando el id (write_only)
    familia_id = serializers.PrimaryKeyRelatedField(queryset=Familia.objects.all(), source='familia', write_only=True)

    class Meta:
        model = Especie
        fields = ['id', 'nombre_vulgar', 'nombre_cientifico', 'familia', 'familia_id', 'en_peligro']


# Serializer para listar Zoológicos con información adicional
class ZoologicoSerializer(serializers.ModelSerializer):
    # Cantidad total de animales en el zoo
    cantidad_animales = serializers.SerializerMethodField()
    # Animales agrupados por familia (ej: Mamíferos: [Tigre, Panda])
    animales_por_familia = serializers.SerializerMethodField()

    class Meta:
        model = Zoo
        fields = ['id', 'nombre', 'ciudad', 'pais', 'tamano_m2', 'presupuesto_anual', 
                  'cantidad_animales', 'animales_por_familia']

    # Devuelve la cantidad total de animales en el zoológico
    def get_cantidad_animales(self, obj):
        return obj.animales.count()

    # Agrupa los animales del zoológico por familia
    def get_animales_por_familia(self, obj):
        agrupados = defaultdict(list)
        for especie in obj.animales.select_related('familia').all():
            familia_nombre = especie.familia.nombre if especie.familia else 'Desconocida'
            agrupados[familia_nombre].append(especie.nombre_vulgar)
        # Retorna un dict con familia -> lista de nombres de especies
        return {familia: nombres for familia, nombres in agrupados.items()}


# Serializer especializado para CREAR y ACTUALIZAR zoológicos
class ZooCrearActualizarSerializer(serializers.ModelSerializer):
    # Lista de nombres científicos que se recibirán en la petición para asociar especies
    animales_cientificos = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False,
        help_text="Lista de nombres científicos de especies a asociar"
    )
    # Los animales se devuelven en modo lectura con detalle
    animales = EspecieSerializer(many=True, read_only=True)

    class Meta:
        model = Zoo
        fields = ['id', 'nombre', 'ciudad', 'pais', 'tamano_m2', 
                  'presupuesto_anual', 'animales_cientificos', 'animales']

    # Limpia la lista de animales científicos (quita espacios y vacíos)
    def validate_animales_cientificos(self, value):
        return [s.strip() for s in value if s and s.strip()]

    # CREATE: crea un zoo y asocia las especies por nombre científico
    @transaction.atomic
    def create(self, validated_data):
        animales_cientificos = validated_data.pop('animales_cientificos', [])
        zoo = Zoo.objects.create(**validated_data)
        if animales_cientificos:
            especies = Especie.objects.filter(nombre_cientifico__in=animales_cientificos)
            encontrados = set(especies.values_list('nombre_cientifico', flat=True))
            faltantes = [s for s in animales_cientificos if s not in encontrados]
            if faltantes:
                raise serializers.ValidationError({
                    'animales_cientificos': f"No existen las siguientes especies: {faltantes}"
                })
            zoo.animales.set(especies)
        return zoo

    # UPDATE: actualiza los campos del zoo y las especies asociadas
    @transaction.atomic
    def update(self, instance, validated_data):
        animales_cientificos = validated_data.pop('animales_cientificos', None)
        # Actualiza atributos básicos del zoo
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        # Si se mandó lista de animales, los valida y asigna
        if animales_cientificos is not None:
            especies = Especie.objects.filter(nombre_cientifico__in=animales_cientificos)
            encontrados = set(especies.values_list('nombre_cientifico', flat=True))
            faltantes = [s for s in animales_cientificos if s not in encontrados]
            if faltantes:
                raise serializers.ValidationError({
                    'animales_cientificos': f"No existen las siguientes especies: {faltantes}"
                })
            instance.animales.set(especies)
        return instance
