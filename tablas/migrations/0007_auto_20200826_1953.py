# Generated by Django 3.1 on 2020-08-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0006_booking_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
