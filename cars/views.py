from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Car
from .serializers import CarSerializer

class CarListView(ListAPIView):
    """
    Vista para listar autos con soporte para filtros, ordenamiento y búsqueda.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['brand', 'year', 'price', 'fuel_type', 'transmission', 'is_available']
    search_fields = ['brand', 'model', 'description']
    ordering_fields = ['price', 'year', 'mileage']


class CarDetailView(RetrieveAPIView):
    """
    Vista para obtener los detalles de un auto específico.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
