from django.db import models
from apps.member.models import Member

from rest_framework import serializers

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Member, related_name='post', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='내용', blank=True)
    balance = models.DecimalField(max_digits=18, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ShortUrl(models.Model):
    short_id = models.CharField(primary_key=True, max_length=16)
    origin_url = models.CharField(max_length=128)
    shorten_url = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    expired = models.DateTimeField(verbose_name="만료 시간")

