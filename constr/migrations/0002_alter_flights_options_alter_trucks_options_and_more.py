# Generated by Django 4.0.5 on 2022-06-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constr', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flights',
            options={'ordering': ['date_Flight'], 'verbose_name': 'Рейс', 'verbose_name_plural': 'Рейсы'},
        ),
        migrations.AlterModelOptions(
            name='trucks',
            options={'ordering': ['brand'], 'verbose_name': 'Самосвал', 'verbose_name_plural': 'Самосвалы'},
        ),
        migrations.AlterModelOptions(
            name='warehouses',
            options={'ordering': ['title'], 'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
        migrations.AlterModelOptions(
            name='сareers',
            options={'ordering': ['title'], 'verbose_name': 'Карьер', 'verbose_name_plural': 'Карьеры'},
        ),
        migrations.AlterField(
            model_name='flights',
            name='date_Flight',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]