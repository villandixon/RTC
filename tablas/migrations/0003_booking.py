# Generated by Django 3.1 on 2020-08-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0002_vanrental'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('TripFrom', models.CharField(max_length=30)),
                ('TripTo', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=5)),
            ],
        ),
    ]
