# Generated by Django 3.0.4 on 2020-11-26 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20201117_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='date_creation',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='category',
            name='user_creation',
        ),
        migrations.RemoveField(
            model_name='category',
            name='user_updated',
        ),
    ]
