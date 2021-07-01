from django.contrib import admin
from .models import Phitube, Category

# Register your models here.

class PhitubeAdmin(admin.ModelAdmin):

    list_display = ("title", 'author',  'description', 'embeded_url', 'published',)

admin.site.register(Phitube, PhitubeAdmin)
admin.site.register(Category)
