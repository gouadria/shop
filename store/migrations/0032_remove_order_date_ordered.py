# Generated by Django 4.2 on 2023-04-17 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_delete_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_ordered',
        ),
    ]
