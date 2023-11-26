from django.db import models


class ExcelData(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
