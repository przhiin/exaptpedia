from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)

    occupation_category = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_column="occupation_category",
        verbose_name="Occupation Category"
    )
    position = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Postion/Organization"
    )
    profile_image = models.ImageField(
        upload_to='user_images/',
        null=True,
        blank=True,
        default='user_images/default.png'
    )

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"


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
