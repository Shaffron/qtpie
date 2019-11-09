from datetime import datetime

from django.db import models


class Annotation(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    order = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'annotation'
        unique_together = ('board', 'order')
        verbose_name = '각주'
        verbose_name_plural = verbose_name


# Create your models here.
class Board(models.Model):
    id = models.BigIntegerField(primary_key=True, default=datetime.now().strftime('%Y%m%d'))
    subject = models.CharField(max_length=100, verbose_name='말씀 주제')
    paragraph = models.CharField(max_length=50, verbose_name='말씀 구절')
    guide = models.CharField(max_length=1000, verbose_name='QT 길잡이')
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'board'
        verbose_name = 'QT 게시글'
        verbose_name_plural = verbose_name


class Contemplation(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    order = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'contemplation'
        unique_together = ('board', 'order')
        verbose_name = '개인묵상'
        verbose_name_plural = verbose_name


class Prayer(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    order = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'prayer'
        unique_together = ('board', 'order')
        verbose_name = '중보기도'
        verbose_name_plural = verbose_name


class Word(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    order = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'word'
        unique_together = ('board', 'order')
        verbose_name = '말씀구절'
        verbose_name_plural = verbose_name
