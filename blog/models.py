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
    name = models.CharField(verbose_name = 'Name', max_length = 256, blank = True, null=True)
    email = models.EmailField(verbose_name ='Email Address')

    def __str__(self):
        return self.email

