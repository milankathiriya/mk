from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=260, null=False, blank=False, unique=True)
    subject = models.CharField(max_length=260, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name + "_" + self.email
