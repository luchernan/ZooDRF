from django.contrib import admin

from django.contrib import admin
from .models import Familia, Especie, Zoologico as Zoo

# Importa y registra los modelos en el panel de administración de Django
# Cada clase configura cómo se verán y gestionarán las entidades en el admin.

# Registro del modelo Familia en el admin
@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    # Define qué campos mostrar en la lista del admin
    list_display = ['nombre']


# Registro del modelo Especie en el admin
@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    # Muestra estas columnas en la vista de lista del admin
    list_display = ['nombre_vulgar', 'nombre_cientifico', 'familia', 'en_peligro']
    # Añade filtros laterales para refinar resultados
    list_filter = ['familia', 'en_peligro']
    # Permite buscar por nombre vulgar o científico en el buscador del admin
    search_fields = ['nombre_vulgar', 'nombre_cientifico']


# Registro del modelo Zoo en el admin
@admin.register(Zoo)
class ZooAdmin(admin.ModelAdmin):
    # Campos que se muestran en la tabla principal del admin
    list_display = ['nombre', 'ciudad', 'pais', 'tamano_m2', 'presupuesto_anual']
    # Habilita el buscador por nombre, ciudad y país
    search_fields = ['nombre', 'ciudad', 'pais']
    # Añade un widget para seleccionar múltiples especies en horizontal (muchos a muchos)
    filter_horizontal = ('animales',)


##Usuario y Contraseña de la base de datos para acceder al panel

##admin
##lucas