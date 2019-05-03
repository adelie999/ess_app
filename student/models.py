""" this student models.py """
import pytz
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Parents(models.Model):
    """ this class parents table """
    db_table = 'parents'
    parent_name = models.CharField('氏名', max_length=30, unique=True)
    parent_email = models.EmailField('メールアドレス', max_length=50)
    payment = models.IntegerField('月謝', default=0)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.parent_name


class Students(models.Model):
    """ this class students table """
    db_table = 'students'
    student_name = models.CharField('氏名', max_length=30)
    student_birthday = models.CharField('生年月日', max_length=8)
    student_age = models.IntegerField(
        '年齢', validators=[MinValueValidator(1), MaxValueValidator(100)])
    student_school_year = models.IntegerField(
        '学年', validators=[MinValueValidator(1), MaxValueValidator(6)], default=1)
    parent_name = models.ForeignKey(
        Parents, on_delete=models.CASCADE, to_field='parent_name', verbose_name='保護者氏名')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.student_name


class Schedule(models.Model):
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
        return super(Schedule, self).save(*args, **kwargs)
