# Generated by Django 4.2.3 on 2023-07-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='type',
            field=models.IntegerField(choices=[(1, 'Checkin'), (2, 'Checkout')]),
        ),
    ]
