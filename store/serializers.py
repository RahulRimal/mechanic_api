
from rest_framework import serializers
from django.db.models import Avg

from .models import Customer, Mechanic, Review, SparePartBillImage, Vehicle, VehicleCategory, VehiclePart, VehicleRepairOverview, VehicleRepairRequest, VehicleRepairRequestImage, VehicleRepairRequestVideo, Workshop, VehicleRepair


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone_number',
                  'username', 'email', 'description', 'image']


class MechanicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Mechanic
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone_number',
                  'username', 'email', 'status', 'description', 'image',
                  'vehicle_speciality', 'vehicle_part_speciality',
                  'average_rating']

    def get_average_rating(self, obj):
        average_rating = Review.objects.filter(mechanic=obj).aggregate(
            avg_rating=Avg('rating')).get('avg_rating')
        return average_rating or 0


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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer', 'mechanic',
                  'rating', 'content', 'created_at']


class VehicleRepairRequestImageSerializer(serializers.ModelSerializer):

    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = VehicleRepairRequestImage
        # fields = ['id','repair_request', 'image']
        fields = ['id', 'images', 'image']

    def create(self, validated_data):
        request_id = self.context['request_id']

        images = [VehicleRepairRequestImage(
            repair_request_id=request_id, image=image
        ) for image in validated_data['images']]

        return VehicleRepairRequestImage.objects.bulk_create(images)


class VehicleRepairRequestVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRepairRequestVideo
#         # fields = ['id','repair_request', 'video']
        fields = ['id', 'video']


class VehicleRepairRequestSerializer(serializers.ModelSerializer):
    images = VehicleRepairRequestImageSerializer(many=True, read_only=True)
    videos = VehicleRepairRequestVideoSerializer(many=True, read_only=True)

    class Meta:
        model = VehicleRepairRequest
        fields = ['id', 'customer', 'location_name', 'location_coordinates',
                  'vehicle', 'vehicle_part', 'description', 'images', 'videos',
                  'created_at']
        # fields = ['id', 'customer','preferred_mechanic', 'location_name',
        # 'location_coordinates', 'vehicle', 'vehicle_part', 'description',
        # 'images', 'videos', 'created_at']


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ['name', 'location', 'woner_name', 'woner_number']


class VehicleRepairOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRepairOverview
        fields = ['problem_name', 'problem_description',
                  'mechanic_charge', 'workshop_needed', 'needs_to_tow', 'estimate_time', 'status']


class SparePartBillImageSerializer(serializers.ModelSerializer):

    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = VehicleRepairRequestImage
        fields = ['id', 'images', 'image']

    def create(self, validated_data):
        repair_id = self.context['repair_id']

        images = [SparePartBillImage(
            vehicle_repair_id=repair_id, image=image
        ) for image in validated_data['images']]

        return SparePartBillImage.objects.bulk_create(images)


class VehicleRepairSerializer(serializers.ModelSerializer):
    bills = SparePartBillImageSerializer(many=True, read_only=True)
    vehicle = VehicleSerializer()
    mechanic = MechanicSerializer()
    customer = CustomerSerializer()
    workshop = WorkshopSerializer()

    class Meta:
        model = VehicleRepair
        fields = ['vehicle', 'mechanic', 'customer',
                  'mechanic_charge', 'workshop', 'bills']
