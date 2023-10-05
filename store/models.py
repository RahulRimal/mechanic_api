import os
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

    MECHANINC_STATUS_AVAILABLE = 'available'
    MECHANINC_STATUS_AWAY = 'away'
    MECHANINC_STATUS_ON_THE_WAY = 'on the way'
    MECHANINC_STATUS_ON_REPAIR_PROCESS = 'on repair process'

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
        (VEHICLE_PART_SEPCIALITY_CHASSIS,
         VEHICLE_PART_SEPCIALITY_CHASSIS.capitalize()),
        (VEHICLE_PART_SEPCIALITY_ELECTRICITY,
         VEHICLE_PART_SEPCIALITY_ELECTRICITY.capitalize()),
        (VEHICLE_PART_SEPCIALITY_OTHER, VEHICLE_PART_SEPCIALITY_OTHER.capitalize()),
    ]

    MECHANINC_STATUS_CHOICES = [
        (MECHANINC_STATUS_AVAILABLE, MECHANINC_STATUS_AVAILABLE.capitalize()),
        (MECHANINC_STATUS_AWAY, MECHANINC_STATUS_AWAY.capitalize()),
        (MECHANINC_STATUS_ON_THE_WAY, MECHANINC_STATUS_ON_THE_WAY.capitalize()),
        (MECHANINC_STATUS_ON_REPAIR_PROCESS,
         MECHANINC_STATUS_ON_REPAIR_PROCESS.capitalize()),
    ]

    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        # upload_to='customer/images', null=True, blank=True)
        upload_to='store/images/mechanic', null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle_speciality = models.CharField(
        max_length=255, choices=VEHICLE_SPECIALITY_CHOICES, null=False,
        blank=False)
    vehicle_part_speciality = models.CharField(
        max_length=255, choices=VEHICLE_PART_SEPCIALITY_CHOICES, null=False,
        blank=False)
    status = models.CharField(
        max_length=100, choices=MECHANINC_STATUS_CHOICES,
        default=MECHANINC_STATUS_AVAILABLE)

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

    name = models.CharField(
        max_length=100, choices=VEHICLE_PART_CHOICES, null=False, blank=False)
    image = models.ImageField(
        upload_to='store/images/vehicle_part', null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name.capitalize())


class Review(models.Model):

    RATING_1_STAR = 1
    RATING_2_STARS = 2
    RATING_3_STARS = 3
    RATING_4_STARS = 4
    RATING_5_STARS = 5

    RATING_CHOICES = [
        (RATING_1_STAR, '1 Star'),
        (RATING_2_STARS, '2 Stars'),
        (RATING_3_STARS, '3 Stars'),
        (RATING_4_STARS, '4 Stars'),
        (RATING_5_STARS, '5 Stars'),
    ]

    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=RATING_1_STAR)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.mechanic.username} for {self.customer.user.username}"


class VehicleRepairRequest(models.Model):
    location_name = models.CharField(max_length=255)
    location_coordinates = models.CharField(max_length=255)
    description = models.TextField()
    preferred_mechanic = models.ForeignKey(
        Mechanic, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle_part = models.ForeignKey(
        VehiclePart, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Vehicle Repair Request by {self.customer.user.username}"


class VehicleRepairRequestImage(models.Model):
    repair_request = models.ForeignKey(
        VehicleRepairRequest, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='store/images/repair_request/images')

    def __str__(self):
        # return str(self.image)
        return os.path.basename(str(self.image))


class VehicleRepairRequestVideo(models.Model):
    repair_request = models.ForeignKey(
        VehicleRepairRequest, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='store/images/repair_request/videos')

    def __str__(self):
        return os.path.basename(str(self.video))


class Workshop(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    woner_name = models.CharField(max_length=255, null=False, blank=False)
    woner_number = models.CharField(
        max_length=10, null=False, blank=False)


class VehicleRepairOverview(models.Model):

    OVERVIEW_STATUS_PENDING = 'pending'
    OVERVIEW_STATUS_ACCEPTED = 'accepted'
    OVERVIEW_STATUS_REJECTED = 'rejected'

    OVERVIEW_STATUS_CHOICES = [
        (OVERVIEW_STATUS_PENDING, OVERVIEW_STATUS_PENDING.capitalize()),
        (OVERVIEW_STATUS_ACCEPTED, OVERVIEW_STATUS_ACCEPTED.capitalize()),
        (OVERVIEW_STATUS_REJECTED, OVERVIEW_STATUS_REJECTED.capitalize()),
    ]

    problem_name = models.CharField(max_length=255, null=False, blank=False)
    problem_description = models.TextField()
    mechanic_charge = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    workshop_needed = models.BooleanField(default=False)
    needs_to_tow = models.BooleanField(default=False)
    estimate_time = models.TimeField()
    status = models.CharField(max_length=20, choices=OVERVIEW_STATUS_CHOICES,
                              default=OVERVIEW_STATUS_PENDING)


class VehicleRepair(models.Model):
    REPAIR_STATUS_ONGOING = 'ongoing'
    REPAIR_STATUS_WAITING_FOR_SPARE_PART = 'waiting for spare part'
    REPAIR_STATUS_COMPLETED = 'completed'

    REPAIR_STATUS_CHOICES = [
        (REPAIR_STATUS_ONGOING, REPAIR_STATUS_ONGOING.capitalize()),
        (REPAIR_STATUS_WAITING_FOR_SPARE_PART,
         REPAIR_STATUS_WAITING_FOR_SPARE_PART.capitalize()),
        (REPAIR_STATUS_COMPLETED, REPAIR_STATUS_COMPLETED.capitalize()),
    ]

    mechanic = models.OneToOneField(Mechanic, on_delete=models.PROTECT)
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.PROTECT)
    workshop = models.OneToOneField(
        Workshop, on_delete=models.PROTECT, null=True, blank=True)
    mechanic_charge = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)


class SparePartBillImage(models.Model):
    image = models.ImageField(
        upload_to='store/images/vehicle_repair', null=False, blank=False)
    vehicle_repair = models.ForeignKey(VehicleRepair, on_delete=models.CASCADE)
