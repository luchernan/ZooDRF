from django.db import models

# Modelo que representa una familia biológica de especies (ej: Félidos, Cánidos, etc.)
class Familia(models.Model):
    # Nombre de la familia, único para evitar duplicados
    nombre = models.CharField(max_length=150, unique=True)

    class Meta:
        # Ordena las familias alfabéticamente por nombre en las consultas
        ordering = ['nombre']

    # Representación en texto (ej: "Félidos")
    def __str__(self):
        return self.nombre


# Modelo que representa una especie animal
class Especie(models.Model):
    # Nombre común o vulgar (ej: "Tigre")
    nombre_vulgar = models.CharField(max_length=200)
    # Nombre científico único (ej: "Panthera tigris")
    nombre_cientifico = models.CharField(max_length=200, unique=True)
    # Relación con la familia a la que pertenece (cada especie pertenece a una familia)
    # PROTECT evita borrar familias si hay especies relacionadas
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT, related_name='especies')
    # Indica si está en peligro de extinción
    en_peligro = models.BooleanField(default=False)

    class Meta:
        # Ordena las especies alfabéticamente por nombre científico
        ordering = ['nombre_cientifico']

    # Representación en texto (ej: "Tigre (Panthera tigris)")
    def __str__(self):
        return f"{self.nombre_vulgar} ({self.nombre_cientifico})"


# Modelo que representa un zoológico
class Zoologico(models.Model):
    # Datos generales del zoo
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=120)
    pais = models.CharField(max_length=120)
    tamano_m2 = models.PositiveIntegerField()  # Tamaño en metros cuadrados
    presupuesto_anual = models.DecimalField(max_digits=12, decimal_places=2)  # Presupuesto en dinero

    # Relación muchos a muchos: un zoo puede tener muchas especies,
    # y una especie puede estar en muchos zoos
    animales = models.ManyToManyField(Especie, related_name='zoos', blank=True)

    # Campos de auditoría
    creado_en = models.DateTimeField(auto_now_add=True)  # Se asigna al crear
    actualizado_en = models.DateTimeField(auto_now=True)  # Se actualiza en cada modificación

    class Meta:
        # Ordena los zoológicos alfabéticamente por nombre
        ordering = ['nombre']

    # Representación en texto (ej: "Zoo de Madrid")
    def __str__(self):
        return self.nombre
