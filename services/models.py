from django.db import models

# Create your models here.
from django.db import models
from users.models import Artisan


class ServiceType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    service_icon = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('suspend', 'Suspend'),
        ('disabled', 'Disabled'),
        ('waiting', 'Waiting'),
    ]

    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='waiting')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class CreatArtisan(models.Model):
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    main_image = models.ImageField(upload_to="artisan_creat/")

    is_active = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class CreatImage(models.Model):
    creat = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="artisan_creat/")

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)



