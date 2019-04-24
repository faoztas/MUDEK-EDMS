from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

PERIOD = (
    ('AUTUMN', _('Güz')),
    ('SPRING', _('Bahar')),
)

COURSESTATUS = (
    ('COMPULSORY', _('Zorunlu')),
    ('OPTIONAL', _('Seçmeli')),
)

POSSESSIVE = (
    ('DEPARTMENT', _('Bölüm Dersi')),
    ('SERVICE', _('Bölüm Dışı')),
)

LANGUAGE = (
    ('TURKISH', _('Türkçe')),
    ('ENGLİSH', _('Ingilizce')),
)


class Faculty(models.Model):
    f_code = models.PositiveIntegerField(verbose_name=_('Fakülte Kodu'))
    f_name = models.CharField(verbose_name=_('Fakülte Adı'), max_length=60)

    def __str__(self):
        return '{name}'.format(name=self.f_name)

    def clean(self):
        temp = Faculty.objects.filter(f_name=self.f_name)
        for i in temp:
            if i.f_name == self.f_name:
                raise ValidationError({'f_name': 'Sisteme kayıtlı.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculty'


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    d_code = models.PositiveIntegerField(verbose_name=_('Bölüm Kodu'))
    d_name = models.CharField(verbose_name=_('Bölüm Adı'), max_length=60)

    def __str__(self):
        return '{faculty} - {d_name}'.format(
            faculty=self.faculty.f_name, d_name=self.d_name
        )

    def clean(self):
        temp = Department.objects.filter(d_name=self.d_name)
        for i in temp:
            if i.d_name == self.d_name:
                raise ValidationError({'d_name': 'Sisteme kayıtlı.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'


class Output(models.Model):
    o_no = models.PositiveIntegerField(verbose_name=_('Çıktı Numarası'))
    o_comment = models.TextField(verbose_name=_('Açıklaması'), max_length=250)
    general_version = models.PositiveIntegerField(verbose_name=_('Genel Sürüm'))
    lower_version = models.PositiveIntegerField(verbose_name=_('Alt Sürüm'))
    side_version = models.PositiveIntegerField(verbose_name=_('Yan Sürüm'))

    def __str__(self):
        return '{o_no} - {o_comment}'.format(
            o_no=self.o_no,
            o_comment=self.o_comment
        )

    def clean(self):
        temp = Output.objects.filter(o_no=self.o_no)
        for i in temp:
            if i.o_no == self.o_no:
                raise ValidationError({'o_no': 'Sisteme kayıtlı.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Output'
        verbose_name_plural = 'Output'


class Lesson(models.Model):
    output = models.ManyToManyField(Output)
    l_code = models.CharField(verbose_name=_('Dersin Kodu'), max_length=10)
    l_name = models.CharField(verbose_name=_('Dersin Adı'), max_length=50)
    l_academician = models.CharField(
        verbose_name=_('Dersin Veren Akademisyen'), max_length=70)
    l_status = models.CharField(
        verbose_name=_('Ders Durumu'), max_length=15, choices=COURSESTATUS)
    l_period = models.CharField(
        verbose_name=_('Ders Dönemi'), max_length=15, choices=PERIOD)
    l_class = models.PositiveIntegerField(verbose_name=_('Ders Sınıfı'))
    l_order = models.PositiveIntegerField(verbose_name=_('Dönemin Kaçıcı Dersi'))
    l_possitive = models.CharField(
        verbose_name=_('Dersin Aitliği'), max_length=25, choices=POSSESSIVE)
    l_language = models.CharField(
        verbose_name=_('Dersin Dili'), max_length=25, choices=LANGUAGE)
    l_ects = models.PositiveIntegerField(verbose_name=_('Ders ECTS'))
    l_akts = models.PositiveIntegerField(verbose_name=_('Ders AKTS'))
    l_credit = models.PositiveIntegerField(verbose_name=_('Ders Kredi'))
    l_theory = models.PositiveIntegerField(verbose_name=_('Ders Teori Saati'))
    l_application = models.PositiveIntegerField(verbose_name=_('Ders Uygulama Saati'))
    l_lab = models.PositiveIntegerField(verbose_name=_('Ders Laboratuvar Saati'))

    def __str__(self):
        return '{l_code} - {l_name} - {l_academician}'.format(
            l_code=self.l_code,
            l_name=self.l_name,
            l_academician=self.l_academician
        )

    def clean(self):
        temp = Lesson.objects.filter(l_code=self.l_code)
        for i in temp:
            if i.l_code == self.l_code:
                raise ValidationError({'l_code': 'Sisteme kayıtlı.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lesson'