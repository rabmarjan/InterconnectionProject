"""
models module for organising table and validation
"""
from django.db import models


class Contact(models.Model):
    """
    A class for storing instance contact
    """
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=130, blank=True, null=True)
    middle_name = models.CharField(max_length=130, blank=True, null=True)
    last_name = models.CharField(max_length=130, blank=True, null=True)
    email = models.EmailField(max_length=110, blank=True, null=True)
    country = models.CharField(max_length=65, blank=True, null=True)
    phone = models.CharField(max_length=19, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
