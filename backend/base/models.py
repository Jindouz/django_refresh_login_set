from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    img_path = models.ImageField(null=True,blank=True,default=None)
   
    def __str__(self):
        return f'{self.name} {self.author} {self.year} {self.user} {self.img_path}'