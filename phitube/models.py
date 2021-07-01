from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('phitube:cat_detail', args=[str(self.id)])

    def __str__(self):
        return self.category

class Phitube(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True, related_name='cat')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    embeded_url = models.CharField(max_length=600)
    banner = models.ImageField(upload_to='phitube', blank=True)
    published = models.DateTimeField(default=timezone.now)
    Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('media_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Phitube, on_delete=models.CASCADE, related_name='vcomments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{} by {} on {}'.format(self.body, self.name, self.post)
