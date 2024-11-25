from django.core.management.base import BaseCommand
from faker import Faker
from cars.models import Car
import random

class Command(BaseCommand):
    help = 'Crea 1000 datos de ejemplo para el catálogo de autos.'

    def handle(self, *args, **kwargs):
        # Instancia de Faker
        faker = Faker()
        
        # Opciones para los campos
        brands = ['Toyota', 'Honda', 'Tesla', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Audi', 'Mercedes']
        colors = ['Red', 'Blue', 'White', 'Black', 'Silver', 'Gray', 'Green', 'Yellow', 'Orange']
        fuel_types = ['Gasoline', 'Diesel', 'Electric', 'Hybrid']
        transmissions = ['automatic', 'manual']

        # Generar 1000 autos
        cars = []
        for _ in range(1000):
            car = Car(
                brand=random.choice(brands),
                model=faker.word().capitalize(),  # Modelo ficticio
                year=random.randint(2000, 2023),  # Año aleatorio
                color=random.choice(colors),
                price=round(random.uniform(5000, 100000), 2),  # Precio aleatorio entre $5,000 y $100,000
                is_available=faker.boolean(chance_of_getting_true=80),  # 80% de probabilidad de estar disponible
                description=faker.sentence(),  # Descripción ficticia
                engine=f"{random.randint(1, 8)}.0L {random.choice(['V6', 'V8', 'I4', 'Electric'])}",  # Motor ficticio
                fuel_type=random.choice(fuel_types),
                mileage=random.randint(0, 200000),  # Kilometraje aleatorio
                transmission=random.choice(transmissions)
            )
            cars.append(car)

        # Insertar los datos en la base de datos
        Car.objects.bulk_create(cars)

        self.stdout.write(self.style.SUCCESS(f'Se crearon 1000 autos de ejemplo con éxito.'))
