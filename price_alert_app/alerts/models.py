from django.db import models
from django.contrib.auth.models import User
import smtpd
from django.core.mail import send_mail
from django.db import models


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
    # updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.status == 'created' and self.current_price >= self.target_price:
            self.status = 'triggered'
            # send email to users
            send_mail(
                'Price Alert!!!',
                f'price alert for {self.currency} has been triggered. Current price is {self.current_price}',
                'ajinkya@gmail.com',
                [self.user.email],
                fail_silently=False
            )
            # print the email
            print(f'Price alert for {self.currency} triggered. Current price: {self.current_price}')
            super().save(*args, **kwargs)