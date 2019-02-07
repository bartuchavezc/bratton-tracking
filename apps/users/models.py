from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.administracion.models import Customer, Vessel

# Create your models here.

class CustomUser(AbstractUser):
        customer = models.OneToOneField(Customer, on_delete=False, null=True)
        is_bratton_admin = models.BooleanField(default=False)
        is_validated = models.BooleanField(default=False)
        def __str__(self):
            return self.email
        class Meta:
            permissions = (("validate_user", "Set is_validated as True"),)
