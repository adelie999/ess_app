""" this student models.py """
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Parents(models.Model):
    """ this class parents table """
    db_table = 'parents'
    parent_name = models.CharField('氏名', max_length=30, unique=True)
    parent_email = models.EmailField('メールアドレス', max_length=50)
    created_at = models.DateTimeField('作成日')
    updated_at = models.DateTimeField('更新日')

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
    created_at = models.DateTimeField('作成日')
    updated_at = models.DateTimeField('更新日')

    def __str__(self):
        return self.student_name
