# Generated by Django 4.2 on 2023-04-17 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_command_date_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_ordered',
        ),
    ]
