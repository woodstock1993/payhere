from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.member import utils
from .managers import CustomUserManager

# Create your models here.
class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=128, blank=False)
    password = models.CharField(max_length=20, validators=[utils.password_validator])
    
    # 관리자 페이지 접근 권한 여부
    is_staff = models.BooleanField(default=False)

    # 해당 계정 활성화 유무
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # interface, DB 활동과 관련, customizing이 필요할 때 접근
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "member"