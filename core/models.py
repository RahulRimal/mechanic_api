# from django.db import models

# from django.contrib.auth.models import AbstractUser
# from rest_framework_simplejwt.tokens import RefreshToken

# # Create your models here.

# AUTH_PROVIDERS = {
#     'email': 'email',
#     'facebook': 'facebook',
#     'google': 'google',
#     'twitter': 'twitter',
#     'github': 'github',
#     'linkedin': 'linkedin',
#     'instagram': 'instagram',
# }


# class User(AbstractUser):
#     USERNAME_FIELD = 'email'
#     email = models.EmailField(unique=True, null=False)
#     auth_provider = models.CharField(
#         max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))
#     REQUIRED_FIELDS = ['username']

#     def __str__(self) -> str:
#         return self.username

#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }


from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
# from rest_framework_simplejwt.tokens import RefreshToken

AUTH_PROVIDERS = {
    'email': 'email',
    'facebook': 'facebook',
    'google': 'google',
    'twitter': 'twitter',
    'github': 'github',
    'linkedin': 'linkedin',
    'instagram': 'instagram',
}


class PhoneNumberUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Create and save a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        normalized_phone_number = self.normalize_phone_number(phone_number)
        user = self.model(phone_number=normalized_phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given phone number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)

    @staticmethod
    def normalize_phone_number(phone_number):
        """
        Normalize the phone number by removing any special characters or formatting.
        """
        # Add any necessary logic to normalize the phone number according to your needs
        # For example, remove spaces, dashes, or other special characters
        normalized_phone_number = phone_number.replace(' ', '').replace('-', '')
        return normalized_phone_number


class User(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    email = models.EmailField('email address', unique=True, blank=True, null=True)
    phone_number = models.CharField('phone number', unique=True, max_length=10)
    auth_provider = models.CharField(
        max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))

    objects = PhoneNumberUserManager()

    def __str__(self) -> str:
        # return self.phone_number
        return self.first_name + ' ' + self.last_name

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     }
