"""Model for Client."""
from django.db import models


class Client(models.Model):
    """Model for Client."""

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    postcode = models.CharField(blank=True, max_length=30)
    state = models.CharField(blank=True, max_length=30)
    street = models.CharField(blank=True, max_length=30)
    suburb = models.CharField(blank=True, max_length=30)
