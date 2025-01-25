
from django.db import models

from config import settings


class Car(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    amount = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = "машины"
        db_table = "cars"


class Moto(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                              related_name="moto")
    title = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "мотоцикл"
        verbose_name_plural = "мотоциклы"
        db_table = "moto"


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True, related_name="milage")
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, blank=True, null=True, related_name="milage")

    milage = models.PositiveIntegerField(verbose_name="пробег")
    year = models.PositiveSmallIntegerField(verbose_name="год")

    def __str__(self):
        return f"{self.moto if self.moto else self.car} - {self.year}"

    class Meta:
        verbose_name = ""
        verbose_name_plural = ""
        ordering = ('-year',)
