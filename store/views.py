from django.shortcuts import render

from .models import Vehicle, VehicleCategory, VehiclePart
from .serializers import CustomerSerializer, VehicleCategorySerializer, VehiclePartSerializer, VehicleSerializer


from store.models import Customer

from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import action


from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from django_filters.rest_framework import DjangoFilterBackend

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


    