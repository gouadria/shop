# Generated by Django 4.2 on 2023-04-17 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_command_date_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='command',
            old_name='date_command',
            new_name='date_command',
        ),
    ]
