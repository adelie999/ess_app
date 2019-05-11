""" home models """
import pytz
from django.db import models
from django.utils import timezone


class Settings(models.Model):
    """ sttings table """
    name = models.CharField('名前', max_length=30)
    url = models.CharField('URL', max_length=100)
    created_at = models.DateTimeField('作成日')
    updated_at = models.DateTimeField('更新日')

    def save(self, *args, **kwargs):
        """ save method override """
        jst_datetime = timezone.localtime().now()
        if not self.id:
            self.created_at = pytz.utc.localize(jst_datetime)
        self.updated_at = pytz.utc.localize(jst_datetime)
        return super().save(*args, **kwargs)
