# Generated by Django 5.1.6 on 2025-03-04 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name='input your dec'),
        ),
    ]
