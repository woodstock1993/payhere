from django.db import models
from apps.member.models import Member

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Member, related_name='post', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='내용', blank=True)
    balance = models.DecimalField(max_digits=18, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)