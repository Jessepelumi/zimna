from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # optional username
    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=True
    )

    # email
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)

    # firstname & lastname
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # auto-generate username from email if empty
        if not self.username and self.email:
            base = self.email.split("@")[0]
            self.username = base

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
