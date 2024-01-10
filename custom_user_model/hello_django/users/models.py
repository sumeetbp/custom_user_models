import datetime
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    public_visibility = models.BooleanField(default=True)
    birth_year = models.PositiveIntegerField(_("birth year"), default=0, null=True, blank=True)
    address = models.TextField(_("address"))
    age = models.PositiveIntegerField(_("age"),default=0, null=True, blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
        