from django.db import models

from django.urls import reverse

from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField

# Create your models here.

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True,
        )

class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank=True, 
        null=True,
        )
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])