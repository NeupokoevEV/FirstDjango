# Generated by Django 4.2.3 on 2023-07-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desription',
            field=models.TextField(default='Базовое описание', max_length=1000),
        ),
    ]
