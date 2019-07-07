from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    location = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Subscription(models.Model):
    name = models.CharField(verbose_name = 'Name (optional) ', max_length = 256, blank = True, null=True)
    email = models.EmailField(verbose_name ='Email Addresse ')

    def __str__(self):
        return self.email

class Events(models.Model):
    event_title = models.CharField(verbose_name = 'Title', max_length = 256)
    event_location = models.CharField(verbose_name = 'Location', max_length = 200)
    event_description = models.TextField(verbose_name = 'Description')
    event_date = models.DateField(blank=True, null = True)

    def __str__(self):
        return self.event_title
