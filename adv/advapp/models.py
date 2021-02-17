from django.db import models


class Advertisement(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
        )
    created = models.DateTimeField(auto_now_add=True)
    link_1 = models.URLField(verbose_name='Ссылка на фото (обязательная)')
    link_2 = models.URLField(
        verbose_name='Ссылка на фото (дополнительная)',
        blank=True
        )
    link_3 = models.URLField(
        verbose_name='Ссылка на фото (дополнительная)',
        blank=True
        )
