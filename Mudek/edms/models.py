# Standart Library
import os

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError



def lesson_directory_path(instance, filename):
    return 'user {0}/{1}'.format(instance.user.email, filename)

def other_directory_path(instance, filename):
    return 'user {0}/{1}'.format(instance.lesson.user.email, filename)


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [
        '.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls'
    ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Lesson(models.Model):
    user = models.ForeignKey(
        verbose_name=_('User'),
        to='users.User',
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    lesson_name = models.CharField(verbose_name=_('Ders Adı'), max_length=150)
    lesson_content = models.TextField(
        verbose_name=_('Ders İçeriği'),
        blank=True
    )
    lesson_content_file = models.FileField(
        verbose_name=_('Ders İçeriği Dosya'), blank=True, null=True,
        upload_to=lesson_directory_path, validators=[validate_file_extension]
    )
    lesson_notes = models.TextField(verbose_name=_('Ders Notu'), blank=True)
    lesson_notes_file = models.FileField(
        verbose_name=_('Ders Notu Dosya'),
        blank=True, null=True,
        upload_to=lesson_directory_path, validators=[validate_file_extension]
    )

    def __str__(self):
        return '{lesson_name}'.format(
            lesson_name=self.lesson_name
        )

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lesson'


class Exam(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )
    exam_type = models.CharField(
        verbose_name=_('Sınav Türü'), max_length=50, blank=True, null=True
    )
    exam_information = models.TextField(
        verbose_name=_('Sınav Hakkında Bilgi'),
        max_length=500, blank=True, null=True
    )
    exam_file = models.FileField(
        verbose_name=_('Sınav Kağıdı Dosya'), blank=True, null=True,
        upload_to=other_directory_path, validators=[validate_file_extension]
    )
    exam_answer_file = models.FileField(
        verbose_name=_('Cevap Anahtarı Dosya'), blank=True, null=True,
        upload_to=other_directory_path, validators=[validate_file_extension]
    )

    def __str__(self):
        return '{lesson} - {exam_type}'.format(
            lesson=self.lesson.lesson_name,
            exam_type=self.exam_type
        )

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exam'


class Requested_Documents(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    d_name = models.CharField(
        verbose_name=_('İstenilen Belge Adı'),
        max_length=100
    )
    d_bool = models.BooleanField(
        verbose_name=_('İstenilen Belge Yüklü mü ?'),
        default=False
    )

    def __str__(self):
        return '{d_name}'.format(
            d_name=self.d_name
        )

    class Meta:
        verbose_name = 'Requested Documents'
        verbose_name_plural = 'Requested Documents'


class Other_Document(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )
    name = models.ForeignKey(
        Requested_Documents,
        on_delete=models.CASCADE
    )

    document = models.FileField(
        verbose_name=_('Dosya'), blank=True, null=True,
        upload_to=other_directory_path, validators=[validate_file_extension]
    )

    def __str__(self):
        return '{name}'.format(
            name=self.name.d_name
        )

    class Meta:
        verbose_name = 'Other Document'
        verbose_name_plural = 'Other Document'



