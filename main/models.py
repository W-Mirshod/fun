from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class RequestsLog(models.Model):
    ip_address = models.GenericIPAddressField()
    browser = models.CharField(max_length=255, blank=True, null=True)
    os = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    is_mobile = models.BooleanField(default=False)
    is_tablet = models.BooleanField(default=False)
    is_pc = models.BooleanField(default=False)
    referred_to = models.TextField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    request_time = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        if self.duration:
            return f"{self.ip_address} ({self.duration}s)"
        else:
            return f"{self.ip_address}"


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'


class Intro(models.Model):
    title = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, blank=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="intro_images")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Intros"

    def __str__(self):
        return f"{self.id}. {self.title}"


class Rates(models.Model):
    rating = models.ForeignKey(Intro, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="rates")
    rate = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Ratings"


class Contacting(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contacting"


class Versions(models.Model):
    version = models.CharField(max_length=55)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Versions"
        ordering = ['created_at']

    def __str__(self):
        return self.version
