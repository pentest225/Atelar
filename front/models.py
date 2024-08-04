from django.db import models

# Create your models here.


class AppAssert(models.Model):
    app_icon = models.FileField(upload_to="app_logo/", max_length=100)
    app_name = models.CharField(max_length=255)
    app_description = models.TextField()
    is_active = models.BooleanField(default=True)
    app_primary_color = models.CharField(max_length=7)  # The main color of application

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.app_name}'


class AppSocialLink(models.Model):
    social_icon = models.CharField(max_length=100)
    social_name = models.CharField(max_length=255)
    social_link = models.URLField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.social_name}:${self.social_link}'


class ContactInfo(models.Model):
    place = models.CharField(max_length=255)
    latitude = models.FloatField(max_length=255)
    longitude = models.FloatField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


class BannerSection(models.Model):
    banner_image = models.FileField(upload_to="front_image/", max_length=100)
    banner_title = models.CharField(max_length=255)
    banner_subtitle = models.CharField(max_length=255,null=True, blank=True)
    banner_description = models.CharField(max_length=255)
    banner_font_color = models.CharField(max_length=7)
    is_header_banner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    link_action = models.URLField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.banner_title}'