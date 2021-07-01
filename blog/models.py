from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog', blank=True)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
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
#
# class reply(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)
#
#     class Meta:
#         ordering = ('created',)
#
#     def __str__(self):
#         return '{} by {} on {}'.format(self.body, self.name, self.post)
