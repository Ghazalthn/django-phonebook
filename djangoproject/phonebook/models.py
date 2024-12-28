from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link contact to a user
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=30)
    number = models.CharField(max_length=13)

    class Meta:
        ordering = ['name']  # Order contacts alphabetically by name
