from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alert(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('deleted', 'Deleted'),
        ('triggered', 'Triggered'),
    )

user = models.ForeignKey(User, on_delete=models.CASCADE)
target_price = models.DecimalField(max_digits=10, decimal_places=2)
status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')

created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)