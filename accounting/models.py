""" accounting models """
import pytz
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Sells(models.Model):
    """ sells table """
    year_month = models.IntegerField(
        '年月', validators=[MinValueValidator(1), MaxValueValidator(999999)])
    sell = models.IntegerField('売上')
    created_at = models.DateTimeField('作成日')
    updated_at = models.DateTimeField('更新日')

    def save(self, *args, **kwargs):
        """ save method override """
        jst_datetime = timezone.localtime().now()
        if not self.id:
            self.created_at = pytz.utc.localize(jst_datetime)
        self.updated_at = pytz.utc.localize(jst_datetime)
        return super().save(*args, **kwargs)
