from django.db import models

class Mbtidata(models.Model):
    name=models.CharField(max_length=10)
    mbti=models.CharField(max_length=10)
    description=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name