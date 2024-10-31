from django.db import models

from config.settings import NULLABLE
from users.models import User


class TimeSection(models.Model):
    time_section = models.CharField(verbose_name='час')

    def __str__(self):
        return self.time_section

    class Meta:
        verbose_name = 'Часовая секция'
        verbose_name_plural = 'Часовые секции'
        ordering = ['time_section']


# Create your models here.
class Table(models.Model):
    number = models.IntegerField(verbose_name='Номер столика')
    seats = models.IntegerField(verbose_name='Количество мест')
    times = models.ManyToManyField(TimeSection, **NULLABLE)

    def __str__(self):
        return f'Столик номер: {self.number}'

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'
        ordering = ['number']


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='заказчик', **NULLABLE) # Чей заказ
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, verbose_name='столик', **NULLABLE) # К какому столику заказывается
    order_time = models.ManyToManyField(TimeSection, verbose_name='время') # В какое время заказывается
    order_confirm = models.BooleanField(default=False, verbose_name='Поле подтверждения бронирования')

    def __str__(self):
        return f'Заказ {self.id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['pk']

