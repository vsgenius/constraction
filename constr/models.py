from django.core.exceptions import ValidationError
from django.db import models
from shapely.geometry import Point, Polygon


class Сareers(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True)
    coordinates = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Карьеры'
        verbose_name = 'Карьер'
        ordering = ['title']


class Trucks(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    capacity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name_plural = 'Самосвалы'
        verbose_name = 'Самосвал'
        ordering = ['brand']


class Warehouses(models.Model):
    title = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Склады'
        verbose_name = 'Склад'
        ordering = ['title']


def validate_coordinates(val):
    pass


class Flights(models.Model):
    date_Flight = models.DateTimeField(verbose_name='Дата рейса')
    truck_id = models.ForeignKey('Trucks', on_delete=models.PROTECT, verbose_name='Самосвал')
    career_id = models.ForeignKey('Сareers', on_delete=models.PROTECT, verbose_name='Карьер')
    warehouse_id = models.ForeignKey('Warehouses', on_delete=models.PROTECT, verbose_name='Склад')
    weight = models.FloatField(verbose_name='Вес')
    coordinates = models.CharField(max_length=50, verbose_name='Координаты выгрузки')
    completed = models.BooleanField(default=True, verbose_name='Рейс завершен')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Рейсы'
        verbose_name = 'Рейс'
        ordering = ['date_Flight']

    # def clean(self):
    #     errors={}
    #     warehouse = Warehouses.objects.filter(id=self.warehouse_id.id)[0].coordinates.split(',')
    #     flight = self.coordinates.split(',')
    #     p = Point(float(warehouse[0]),float(warehouse[1]))
    #     p2 = Point(float(flight[0]),float(flight[1]))
    #     d = Point(p).distance(p2)
    #     if d > 0.005:
    #         errors['coordinates'] = ValidationError('Координаты рейса не соответствуют заданному Складу')
    #     print(d)
