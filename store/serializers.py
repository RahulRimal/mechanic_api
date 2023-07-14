
from rest_framework import serializers

from .models import Customer, Vehicle, VehicleCategory

class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = [ 'id', 'user_id', 'first_name', 'last_name', 'phone_number',
        
                  'username', 'email', 'description', 'image', 'created_at']



class VehicleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleCategory
        fields = ['id', 'name', 'image']


class VehicleSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'category', 'image']
