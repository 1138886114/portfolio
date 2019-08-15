from django.db import models

# Create your models here.



class Gallery(models.Model):
    description = models.CharField(default='这是作品的简介',max_length=80)
    image = models.ImageField(default='default.png',upload_to='image/')
    title = models.CharField(default='标题',max_length=20)

    def __str__(self):
        return self.title
