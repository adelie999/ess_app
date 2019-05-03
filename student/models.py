""" this student models.py """
import pytz
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Students(models.Model):
    """ this class students table """
    db_table = 'students'
    name = models.CharField('氏名', max_length=30)
    birthday = models.CharField('生年月日', max_length=8)
    age = models.IntegerField(
        '年齢', validators=[MinValueValidator(1), MaxValueValidator(100)], default=7)
    school_year = models.IntegerField(
        '学年', validators=[MinValueValidator(1), MaxValueValidator(6)], default=1)
    address = models.CharField('住所', max_length=100, default='東京都')
    photo_path = models.ImageField('写真のパス', upload_to='images')
    payment = models.IntegerField('月謝', default=0)
    parent_name = models.CharField('保護者氏名', max_length=30)
    parent_email = models.EmailField('メールアドレス', max_length=50, default="example@aaa.com")
    parent_phone = models.CharField('電話番号', max_length=11, default='00000000000')
    created_at = models.DateTimeField('作成日')
    updated_at = models.DateTimeField('更新日')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ this override save """
        jst_datetime = timezone.localtime().now()
        if not self.id:
            self.created_at = pytz.utc.localize(jst_datetime)
        self.updated_at = pytz.utc.localize(jst_datetime)
        return super().save(*args, **kwargs)


class Schedules(models.Model):
    """ this class schedule table """
    db_table = 'schedule'
    title = models.CharField('タイトル', max_length=50)
    start_date = models.DateTimeField('開始日')
    end_date = models.DateTimeField('終了日')
    description = models.TextField('予定の内容')
    created_at = models.DateTimeField('作成日')
    updated_at = models.DateTimeField('更新日')

    def save(self, *args, **kwargs):
        """ this override save """
        jst_datetime = timezone.localtime().now()
        if not self.id:
            self.created_at = pytz.utc.localize(jst_datetime)
        self.updated_at = pytz.utc.localize(jst_datetime)
        return super().save(*args, **kwargs)
