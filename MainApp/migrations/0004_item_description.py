# Generated by Django 4.2.3 on 2023-07-13 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_remove_item_desription'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Базовое описание', max_length=1000),
        ),
    ]
