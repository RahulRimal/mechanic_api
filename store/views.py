from django.shortcuts import render

from .models import Mechanic, Review, Vehicle, VehicleCategory, VehiclePart, VehicleRepairRequest, VehicleRepairRequestImage
from .serializers import CustomerSerializer, MechanicSerializer, ReviewSerializer, VehicleCategorySerializer, VehiclePartSerializer, VehicleRepairRequestImageSerializer, VehicleRepairRequestSerializer, VehicleSerializer


from store.models import Customer

from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import action


from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter

from rest_framework.response import Response

# Create your views here.



class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.select_related('user').all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



class MechanicViewSet(ModelViewSet):
    queryset = Mechanic.objects.select_related('user').all()
    serializer_class = MechanicSerializer

    # filter_backends = [ DjangoFilterBackend, SearchFilter]
    filter_backends = [ DjangoFilterBackend]
    filterset_fields = ['vehicle_speciality', 'vehicle_part_speciality']

    @action(detail=False, methods=['GET', 'PUT', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (mechanic, created) = Mechanic.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = MechanicSerializer(mechanic)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = MechanicSerializer(mechanic, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



class VehicleCategoryViewSet(ModelViewSet):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer



class VehiclePartViewSet(ModelViewSet):
    # queryset = VehiclePart.objects.all()
    serializer_class = VehiclePartSerializer
    def get_queryset(self):
        return VehiclePart.objects.filter(vehicle_id=self.kwargs['vehicle_pk'])


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category_id']


    

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class VehicleRepairRequestViewSet(ModelViewSet):
    queryset = VehicleRepairRequest.objects.all()
    serializer_class = VehicleRepairRequestSerializer


class VehicleRepairRequestImageViewSet(ModelViewSet):
    def get_queryset(self):
        return VehicleRepairRequestImage.objects.filter(repair_request_id=self.kwargs['repair_request_pk'])
    serializer_class = VehicleRepairRequestImageSerializer
    def get_serializer_context(self):
        return {'request_id': self.kwargs['repair_request_pk']}

