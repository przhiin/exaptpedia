from django.db import models

# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length = 255,)
    description = models.TextField(max_length = 1000,blank = True, null = True)
    date = models.DateField(blank = True, null = True)
    time = models.TimeField(blank = True, null = True)
    location = models.CharField(max_length = 255,blank = True, null = True)
    banner = models.ImageField(upload_to='event_banners/', blank = True, null = True)
    registration_link = models.URLField(max_length = 500, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f"{self.title} on {self.date}"

