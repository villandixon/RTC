# Generated by Django 3.1 on 2020-08-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VanRental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('rental', models.FloatField()),
            ],
        ),
    ]
