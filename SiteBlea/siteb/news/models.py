from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50, help_text='150x150px')
    img = models.ImageField(upload_to='images')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'novosti'
        verbose_name_plural = 'novosti'

