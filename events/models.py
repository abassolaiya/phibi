from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    venue = models.CharField(max_length=450)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='event', blank=True)
    description = models.TextField()
    time = models.CharField(max_length=250)
    published = models.DateTimeField(default=timezone.now)
    Created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])


# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset()\
#         .filter(status='published')

class Resistration(models.Model):
    # objects = models.Manager() # The default manager.
    # published = PublishedManager() # Our custom manager.
    HOW_CHOICES = (
        ('Faecebook', 'Faecebook'),
        ('Twitter', 'Twitter'),
        ('Friend or Colleague', 'Friend or Colleague'),
        ('Google', 'Google'),
        ('Website', 'Website'),
        ('Instagram', 'Instagram'),
        ('News Article', 'News Article'),
        ('LinkedIn', 'LinkedIn'),
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', blank=True, null=True)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='register')
    phone_number = models.CharField(max_length=80)
    address =models.TextField()
    how_did_you_hear_about_this_event = models.CharField(max_length=20,
        choices=HOW_CHOICES, default='Website')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'regiter {} on {}'.format(self.name, self.address)
