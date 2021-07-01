from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not Specified'),)

    STATUS_CHOICES = (
        ('premium', 'Premium'),
        ('intern', 'Intern'),
        ('basic', 'Basic'),
        ('regular', 'Regular'),
        ('admin', 'Admin'),)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, blank=True)
    photo = models.ImageField(upload_to= 'users/%Y/%m/%d/', blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    last_modeified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)



class Contactus(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_no = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{} by {} on {}'.format(self.name, self.name, self.message)
