from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=128, blank=False,)
    mobile = models.BigIntegerField(null = True)
    email = models.EmailField(max_length = 254)
    transaction_id = models.BigIntegerField(null = False)

class Donation(models.Model):
    transaction_id = models.BigIntegerField(null = False)
    donor_id = models.BigIntegerField(null = False)
    project_id = models.BigIntegerField(null = False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null = False)
    time = models.TimeField(auto_now = True)