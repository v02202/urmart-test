# Generated by Django 3.1.4 on 2020-12-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_pcs',
            field=models.PositiveIntegerField(default=0),
        ),
    ]