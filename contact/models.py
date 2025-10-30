from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    is_doctor = models.BooleanField(default=False)
    occupation = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically set occupation if the user is a doctor
        if self.is_doctor:
            self.occupation = 'Doctor'
        elif not self.occupation:  
            # Optional: clear or leave empty if not a doctor
            self.occupation = ''
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
