from django.urls import path
from .views import CarListView, CarDetailView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]
