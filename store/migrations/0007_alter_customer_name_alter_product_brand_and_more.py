# Generated by Django 4.1.4 on 2022-12-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='Brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.CharField(max_length=50),
        ),
    ]
