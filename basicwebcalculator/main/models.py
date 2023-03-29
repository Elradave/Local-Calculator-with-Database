from django.db import models
# Create your models here.


class History(models.Model):
    first_number = models.IntegerField()
    operation = models.CharField(max_length=2)
    second_number = models.IntegerField()
    ans = models.IntegerField()
