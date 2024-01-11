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
    upload = models.FileField(upload_to="users/", max_length=250, null=True, default=None)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UploadedFileMetadata(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    upload = models.FileField(upload_to="users/", max_length=250, null=True, default=None)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    visibility = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    year_of_publish = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Uploaded File Metadata"
