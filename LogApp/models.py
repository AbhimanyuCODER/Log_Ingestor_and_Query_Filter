from django.contrib.postgres.fields import JSONField
from django.db import models

class Log(models.Model):
    traceId = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    message = models.TextField()
    resourceId = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    spanId = models.CharField(max_length=50)
    commit = models.CharField(max_length=50)
    metadata = models.JSONField(default=dict)
