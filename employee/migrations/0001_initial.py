# Generated by Django 4.2.3 on 2023-07-17 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('mood', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
