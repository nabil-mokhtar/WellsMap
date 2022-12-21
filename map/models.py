from django.db import models
from django_countries.fields import CountryField


class Well(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name='اسم البئر')
    information = models.TextField(null=False, blank=False, verbose_name='معلومات حول البئر')
    latitude = models.FloatField(null=True, blank=True, verbose_name='دوائر العرض')
    longitude = models.FloatField(null=True, blank=True, verbose_name='خطوط الطول')
    thumbnailImage = models.TextField(null=True, blank=True, verbose_name='صورة البئر')
    extraImages = models.TextField(null=True, blank=True, verbose_name='صور اضافيه')
    country = CountryField(verbose_name='الدوله')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "البئر"

        verbose_name_plural = "الآبار"
