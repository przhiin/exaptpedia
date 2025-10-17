from django.db import models

# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 255)
    banner = models.ImageField(upload_to='event_banners/', blank = True, null = True)
    registration_link = models.URLField(max_length = 500, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f"{self.title} on {self.date}"

