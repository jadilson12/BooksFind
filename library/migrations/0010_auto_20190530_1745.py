# Generated by Django 2.2.1 on 2019-05-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20190530_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationbook',
            name='idUser',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservationbook',
            name='idbook',
            field=models.IntegerField(blank=True),
        ),
    ]