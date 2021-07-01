from django.contrib import admin

from .models import  Resistration, Event

# Register your models here.
class RegisterFormInline(admin.TabularInline):
    model = Resistration

class EventAdmin(admin.ModelAdmin):
    inlines = [
        RegisterFormInline,
    ]
    list_display = ("title", 'author', 'banner', 'venue',)

admin.site.register(Event, EventAdmin)
