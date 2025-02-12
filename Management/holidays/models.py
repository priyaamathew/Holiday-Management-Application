from django.db import models



class Holiday(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    country = models.CharField(max_length=10)
    type = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



