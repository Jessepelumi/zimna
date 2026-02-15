from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# custom user manager to create admin superuser
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

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
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

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
    
    # attach custom user manager to user
    objects = UserManager()
