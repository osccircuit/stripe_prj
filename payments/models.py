from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")

    def __str__(self):
        return str(self.name).capitalize()