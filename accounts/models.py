from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER=[
    ('Male','Male'),
    ('Female','Female'),
    ('Non-Binary','Non-Binary')
]

class CustomUser(AbstractUser):
    first_name = None  
    last_name = None
    name = models.CharField(max_length = 255, null= False, blank = False)
    phone = models.CharField(max_length=255, blank=True, default='')
    age = models.IntegerField(null=True, blank=True)
    is_doctor = models.BooleanField(default=False, verbose_name="Is a Doctor?")
    occupation = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='user_images/', 
        null=True, 
        blank=True,
        default='user_images/default.png'
    )
    
    def save(self, *args, **kwargs):
        # Automatically set occupation if the user is a doctor
        if self.is_doctor:
            self.occupation = 'Doctor'
        super().save(*args, **kwargs)



    def __str__(self):
        return "name:" + self.name
 
