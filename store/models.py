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


class Mechanic(models.Model):

    VEHICLE_SPECIALITY_BIKE = 'bike'
    VEHICLE_SPECIALITY_CAR = 'car'
    VEHICLE_SPECIALITY_SEMI = 'semi'
    VEHICLE_SPECIALITY_HEAVY = 'heavy'
    VEHICLE_SPECIALITY_MACHINERY = 'machinery'

    VEHICLE_PART_SEPCIALITY_WHEEL = 'wheel'
    VEHICLE_PART_SEPCIALITY_ENGINE = 'engine'
    VEHICLE_PART_SEPCIALITY_BODY = 'body'
    VEHICLE_PART_SEPCIALITY_CHASSIS = 'chassis'
    VEHICLE_PART_SEPCIALITY_ELECTRICITY = 'electricity' 
    VEHICLE_PART_SEPCIALITY_OTHER = 'other'


    VEHICLE_SPECIALITY_CHOICES = [
        (VEHICLE_SPECIALITY_BIKE, VEHICLE_SPECIALITY_BIKE.capitalize()),
        (VEHICLE_SPECIALITY_CAR, VEHICLE_SPECIALITY_CAR.capitalize()),
        (VEHICLE_SPECIALITY_SEMI, VEHICLE_SPECIALITY_SEMI.capitalize()),
        (VEHICLE_SPECIALITY_HEAVY, VEHICLE_SPECIALITY_HEAVY.capitalize()),
        (VEHICLE_SPECIALITY_MACHINERY, VEHICLE_SPECIALITY_MACHINERY.capitalize()),
    ]

    VEHICLE_PART_SEPCIALITY_CHOICES = [
        (VEHICLE_PART_SEPCIALITY_WHEEL, VEHICLE_PART_SEPCIALITY_WHEEL.capitalize()),
        (VEHICLE_PART_SEPCIALITY_ENGINE, VEHICLE_PART_SEPCIALITY_ENGINE.capitalize()),
        (VEHICLE_PART_SEPCIALITY_BODY, VEHICLE_PART_SEPCIALITY_BODY.capitalize()),
        (VEHICLE_PART_SEPCIALITY_CHASSIS, VEHICLE_PART_SEPCIALITY_CHASSIS.capitalize()),
        (VEHICLE_PART_SEPCIALITY_ELECTRICITY, VEHICLE_PART_SEPCIALITY_ELECTRICITY.capitalize()),
        (VEHICLE_PART_SEPCIALITY_OTHER, VEHICLE_PART_SEPCIALITY_OTHER.capitalize()),
        ]

    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        # upload_to='customer/images', null=True, blank=True)
        upload_to='store/images/mechanic', null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle_speciality = models.CharField( max_length=255, choices=VEHICLE_SPECIALITY_CHOICES, null=False, blank=False)
    vehicle_part_speciality = models.CharField( max_length=255, choices=VEHICLE_PART_SEPCIALITY_CHOICES, null=False, blank=False)

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
    CATEGORY_BIKE = 'bike'
    CATEGORY_CAR = 'car'
    CATEGORY_BUS = 'bus'
    CATEGORY_SEMI = 'semi'
    CATEGORY_HEAVY = 'heavy'
    CATEGORY_MACHINERY = 'machinery'

    CATEGORY_CHOICES = [
        (CATEGORY_BIKE, CATEGORY_BIKE.capitalize()),
        (CATEGORY_CAR, CATEGORY_CAR.capitalize()),
        (CATEGORY_BUS, CATEGORY_BUS.capitalize()),
        (CATEGORY_SEMI, CATEGORY_SEMI.capitalize()),
        (CATEGORY_HEAVY, CATEGORY_HEAVY.capitalize()),
        (CATEGORY_MACHINERY, CATEGORY_MACHINERY.capitalize()),
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
    VEHICLE_PART_WHEEL = 'wheel'
    VEHICLE_PART_ENGINE = 'engine'
    VEHICLE_PART_BODY = 'body'
    VEHICLE_PART_CHASSIS = 'chassis'
    VEHICLE_PART_ELECTRICITY = 'electricity'
    VEHICLE_PART_OTHER = 'other'

    VEHICLE_PART_CHOICES = [
        (VEHICLE_PART_WHEEL, VEHICLE_PART_WHEEL.capitalize()),
        (VEHICLE_PART_ENGINE, VEHICLE_PART_ENGINE.capitalize()),
        (VEHICLE_PART_BODY, VEHICLE_PART_BODY.capitalize()),
        (VEHICLE_PART_CHASSIS, VEHICLE_PART_CHASSIS.capitalize()),
        (VEHICLE_PART_ELECTRICITY, VEHICLE_PART_ELECTRICITY.capitalize()),
        (VEHICLE_PART_OTHER, VEHICLE_PART_OTHER.capitalize()),
        
    ]

    name = models.CharField(max_length=100, choices=VEHICLE_PART_CHOICES, null=False, blank=False)
    image = models.ImageField(
        upload_to='store/images/vehicle_part', null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)