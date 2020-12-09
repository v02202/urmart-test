# Generated by Django 3.1.4 on 2020-12-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='shop_id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='order_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='qty',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]