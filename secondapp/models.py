from django.db import models
from mbtiapp.models import User
from file.models import Mbtidata

# Create your models here.
# class Detail(models.Model):
#     content=models.ManyToManyField(Mbtidata, through='ContentView')


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class NameDetail(models.Model):
    name = models.ForeignKey(Mbtidata, on_delete=models.CASCADE)

class MbtiDetail(models.Model):
    mbti = models.ForeignKey(Mbtidata, on_delete=models.CASCADE)

class DescDetail(models.Model):
    desc = models.ForeignKey(Mbtidata, on_delete=models.CASCADE)

