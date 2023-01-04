from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목
    content = models.TextField()  # 내용

    created_at = models.DateTimeField(auto_now_add=True)  # 작성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일
    # author : 추후 작성 예정       # 작성자 정보

    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.pk}]{self.title}"  # [해당 포스트의 pk값]해당 포스트의 title 값

from django.contrib.auth.models import User
class Write(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    



