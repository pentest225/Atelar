from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

SEX = [
    ('h', 'Homme'),
    ('f', 'Femme'),
]


class Profile(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('artisan', 'Artisan'),
        ('admin', 'Admin'),
    ]
    ACCOUNT_STATUS = [
        ('active', 'Actif'),
        ('unactive', 'Deactivé'),
        ('suspend', 'Suspendu'),
        ('wating', 'En Attante'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS, default='active')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Artisan(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="artisan_profile_image", null=True, blank=True)
    sector = models.CharField(max_length=255)  #
    bio = models.TextField(null=True, blank=True)
    sex = models.CharField(max_length=20, choices=SEX, default='h')
    city = models.CharField(max_length=255, null=True, blank=True)
    location_lat = models.CharField(max_length=255, null=True, blank=True)
    location_lon = models.CharField(max_length=255, null=True, blank=True)
    study_level = models.CharField(max_length=255, null=True, blank=True)
    has_study_certify = models.BooleanField(default=False)
    WhatsApp_phone = models.CharField(max_length=10, null=True, blank=True)
    service_average = models.IntegerField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.user.username} - {self.sector}'


class NewsLatter(models.Model):
    email = models.EmailField(max_length=254)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class ContactUs(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

