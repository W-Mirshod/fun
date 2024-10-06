from django.contrib.auth.models import AbstractUser
from django.db import models


class RequestsLog(models.Model):
    ip_address = models.GenericIPAddressField()
    browser = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    referred_to = models.TextField(blank=True, null=True)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.ip_address} on {self.request_time}"


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)


class Ratings(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Intros"

    def __str__(self):
        return self.title


class Rates(models.Model):
    rating = models.ForeignKey(Ratings, on_delete=models.CASCADE)
    rate = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Ratings"
