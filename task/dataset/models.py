from django.db import models


# Model class Dataset to store the data
class Dataset(models.Model):
    date = models.CharField(max_length=10, blank=False, null=False)
    channel = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=10, blank=False, null=False)
    os = models.CharField(max_length=100, blank=False, null=False)
    impressions = models.IntegerField(blank=False, null=False)
    clicks = models.IntegerField(blank=False, null=False)
    installs = models.IntegerField(blank=False, null=False)
    spend = models.FloatField(blank=False, null=False)
    revenue = models.FloatField(blank=False, null=False)
