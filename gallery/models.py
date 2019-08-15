from django.db import models

# Create your models here.



class Gallery(models.Model):
    description = models.CharField(max_length=80)

    # def __str__(self):
    #     pass
