import datetime

from django.db import models

# Create your models here.
class BlogData(models.Model):
    hedding=models.CharField(max_length=100)
    content=models.CharField(max_length=1000)
    auther=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.date.today())
    img=models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.hedding
