import datetime
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    public_visibility = models.BooleanField(default=False)
    birth_year = models.CharField(max_length=100)
    address = models.TextField(_("address"))
    age = models.PositiveIntegerField(_("age"), default=0, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
