from django.db import models

# Create your models here.
class Shorts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=50)
    star = models.IntegerField()
    content = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'shorts'