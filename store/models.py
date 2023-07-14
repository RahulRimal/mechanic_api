from django.conf import settings
from django.db import models


class Customer(models.Model):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        # upload_to='customer/images', null=True, blank=True)
        upload_to='store/images/customer', null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # phone = models.CharField(max_length=10, null=True, blank=True)

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name
    
    def phone_number(self):
        return self.user.phone_number
    


    def email(self):
        return self.user.email

    def username(self):
        return self.user.username

    def created_at(self):
        return self.user.date_joined

    def __str__(self):
        return f"{self.user.id} => {self.user.first_name} {self.user.last_name}"



class VehicleCategory(models.Model):
    CATEGORY_BIKE = 'Bike'
    CATEGORY_CAR = 'Car'
    CATEGORY_BUS = 'Bus'
    CATEGORY_SEMI = 'Semi'
    CATEGORY_HEAVY = 'Heavy'
    CATEGORY_MACHINERY = 'Machinery'

    CATEGORY_CHOICES = [
        (CATEGORY_BIKE, CATEGORY_BIKE),
        (CATEGORY_CAR, CATEGORY_CAR),
        (CATEGORY_BUS, CATEGORY_BUS),
        (CATEGORY_SEMI, CATEGORY_SEMI),
        (CATEGORY_HEAVY, CATEGORY_HEAVY),
        (CATEGORY_MACHINERY, CATEGORY_MACHINERY),
    ]

    # VEHICLE_TYPE_TWO_WHEELER = '2'
    # VEHICLE_TYPE_FOUR_WHEELER = '4'
    # VEHICLE_TYPE_SIX_WHEELER = '6'
    # VEHICLE_TYPE_EIGHT_WHEELER = '8'
    # VEHICLE_TYPE_ELEVEN_WHEELER = '12'
    # VEHICLE_TYPE_CHOICES = [
    #     (VEHICLE_TYPE_TWO_WHEELER, '2 wheeler'),
    #     (VEHICLE_TYPE_FOUR_WHEELER, '4 wheeler'),
    #     (VEHICLE_TYPE_SIX_WHEELER, '6 wheeler'),
    #     (VEHICLE_TYPE_EIGHT_WHEELER, '8 wheeler'),
    #     (VEHICLE_TYPE_ELEVEN_WHEELER, '12 wheeler'),
    # ]

    name = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, blank=False, null=False,)
    image = models.ImageField(
        upload_to='store/images/vehicle_category', null=False, blank=False)
    # type = models.CharField(max_length=2, choices=VEHICLE_TYPE_CHOICES, null=False, blank=True)
    
    
    def __str__(self):
        return self.name





class Vehicle(models.Model):
    

    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='store/images/vehicle', null=False, blank=False)
    category = models.ForeignKey(VehicleCategory, on_delete=models.PROTECT)
    
    

    def __str__(self):
        return self.name



class VehiclePart(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='store/images/vehicle_part', null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)