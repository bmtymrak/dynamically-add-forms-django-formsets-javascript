from django.db import models


class Bird(models.Model):
    common_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)

    class Meta:
        def __str__(self):
            return self.common_name
