from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="accounts/profile_pictures/%y/%m/%d", null=True, blank=True,
                                        default="/accounts/profile.avif")

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.username
