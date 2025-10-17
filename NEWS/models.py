from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False, help_text="Show this at the top of the news list")


    def __str__(self):
        return title

class Announcement(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    poster = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False, help_text="Show this at the top of the news list")

    
    def __str__(self):
        return title