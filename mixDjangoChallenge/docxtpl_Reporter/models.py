from django.db import models
import os
# Create your models here.


class Report(models.Model):
    firma = models.ImageField(verbose_name="Firma Digital")
