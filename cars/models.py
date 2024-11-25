from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)  # Marca
    model = models.CharField(max_length=100)  # Modelo
    year = models.PositiveIntegerField()      # Año
    color = models.CharField(max_length=50)   # Color
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    is_available = models.BooleanField(default=True)  # Disponibilidad
    description = models.TextField(null=True, blank=True)  # Descripción
    engine = models.CharField(max_length=100, null=True, blank=True)  # Tipo de motor
    fuel_type = models.CharField(max_length=50, null=True, blank=True)  # Tipo de combustible
    mileage = models.PositiveIntegerField(null=True, blank=True)  # Kilometraje
    transmission = models.CharField(
        max_length=50,
        choices=[('automatic', 'Automática'), ('manual', 'Manual')],
        default='manual'
    )  # Transmisión

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
