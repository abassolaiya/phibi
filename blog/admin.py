from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class CommonInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommonInline,
    ]
    list_display = ("title", 'author', 'image', 'published',)

admin.site.register(Post, PostAdmin)
# admin.site.register(reply)
