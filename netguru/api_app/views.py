from django.shortcuts import render
from rest_framework import generics
from .serializers import CarCreateSerializer, CarListSerializer, CarRatingSerializer
from .models import Cars
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarCreateSerializer


class CarRatingView(generics.RetrieveUpdateAPIView):
    serializer_class = CarRatingSerializer
    queryset = Cars.objects.all()


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Cars.objects.all()
    permission_classes = (IsAuthenticated, )


class CarsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarCreateSerializer
    queryset = Cars.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

