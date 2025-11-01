from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20,blank = True, null = True)
    email = models.EmailField(max_length=255,blank = True, null = True)

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
        verbose_name="Postion and Organization/Company"
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


    def __str__(self):
        return self.name
