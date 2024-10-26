from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('author', 'Author'),
    ]
    
    email = models.EmailField(unique=True, blank=False)  # Enforces email uniqueness and validation
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # Role to distinguish Admin and Author
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Phone number must be exactly 10 digits')],
        blank=False
    )
    address = models.CharField(max_length=255, blank=True)  # Optional
    city = models.CharField(max_length=50, blank=True)      # Optional
    state = models.CharField(max_length=50, blank=True)     # Optional
    country = models.CharField(max_length=50, blank=True)   # Optional
    pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator(r'^\d{6}$', 'Pincode must be exactly 6 digits')],
        blank=False
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Optional Category model

    def __str__(self):
        return self.name


class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'author'})
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='documents/')
    categories = models.ManyToManyField(Category, blank=True)  # Allows multiple categories per content
