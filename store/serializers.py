
from rest_framework import serializers

from .models import Customer, Mechanic, Vehicle, VehicleCategory, VehiclePart

class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = [ 'id', 'user_id', 'first_name', 'last_name', 'phone_number',
        
                  'username', 'email', 'description', 'image']


class MechanicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Mechanic
        fields = [ 'id', 'user_id', 'first_name', 'last_name', 'phone_number', 'username', 'email', 'description', 'image', 'vehicle_speciality', 'vehicle_part_speciality']



class VehicleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleCategory
        fields = ['id', 'name', 'image']


class VehiclePartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VehiclePart
        fields = ['id', 'name', 'vehicle', 'image']
        # fields = ['id', 'name', 'image']



class VehicleSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'category', 'image']
