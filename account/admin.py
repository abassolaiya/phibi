from django.contrib import admin

from .models import Profile, Contactus

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'date_of_birth', 'photo']

admin.site.register(Contactus)