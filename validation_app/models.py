from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    gst_number = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
