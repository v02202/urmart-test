# Generated by Django 3.1.4 on 2020-12-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201205_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='qty',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
