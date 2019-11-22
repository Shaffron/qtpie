from django.db import models


class User(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=10, null=False, blank=False, db_index=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        db_table = 'user'
        default_related_name = 'users'
        verbose_name = '고객 계정'
