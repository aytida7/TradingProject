# Generated by Django 4.1.4 on 2023-02-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_csvmodel_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvmodel',
            name='volume',
            field=models.FloatField(default=0),
        ),
    ]