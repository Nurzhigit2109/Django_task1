# Generated by Django 3.2.9 on 2021-11-30 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_data_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='created',
        ),
    ]
