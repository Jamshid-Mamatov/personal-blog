from django.db import models
from django.db.models.fields import CharField, TextField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Post(models.Model):
    tittle=CharField(max_length=30)
    text=TextField(max_length=100)
    author=ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.tittle
