# Generated by Django 4.2 on 2023-04-17 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_remove_order_date_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='date_command',
        ),
    ]
