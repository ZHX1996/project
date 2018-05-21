from django.db import models

# Create your models here.
class test(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=20)
    ID = models.IntegerField()
    class Meta:
        db_table = 'test'
