""" schedule models """
import pytz
from django.db import models
from django.utils import timezone


class Schedules(models.Model):
    """ schedules table """
    title = models.CharField('タイトル', max_length=50)
    start_date = models.DateTimeField('開始日')
    end_date = models.DateTimeField('終了日')
    description = models.TextField('予定の内容')
    created_at = models.DateTimeField('作成日')
    updated_at = models.DateTimeField('更新日')

    def save(self, *args, **kwargs):
        """ save method override """
        jst_datetime = timezone.localtime().now()
        if not self.id:
            self.created_at = pytz.utc.localize(jst_datetime)
        self.updated_at = pytz.utc.localize(jst_datetime)
        return super().save(*args, **kwargs)
