from datetime import datetime

from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255, unique=True, verbose_name='email 주소')
    name = models.CharField(max_length=20, db_index=True, null=False, blank=False, verbose_name='이름')
    subscribe = models.BooleanField(default=True, null=False, blank=False, verbose_name='큐티 구독여부')
    active = models.BooleanField(default=True, verbose_name='계정 활성화 여부')
    admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    created = models.DateTimeField(
        default=datetime.now(), null=False, blank=False, auto_now_add=True, verbose_name='생성일'
    )
    updated = models.DateTimeField(default=datetime.now(), null=False, blank=False, auto_now=True, verbose_name='수정일')

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        db_table = 'user'
        default_related_name = 'users'
        verbose_name = 'User'
        verbose_name_plural = f'{verbose_name}s'
