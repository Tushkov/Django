# Generated by Django 5.0.6 on 2024-06-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Регион'),
        ),
    ]
