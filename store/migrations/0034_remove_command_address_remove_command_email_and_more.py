# Generated by Django 4.2 on 2023-04-17 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_order_date_ordered_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='address',
        ),
        migrations.RemoveField(
            model_name='command',
            name='email',
        ),
        migrations.RemoveField(
            model_name='command',
            name='pays',
        ),
        migrations.RemoveField(
            model_name='command',
            name='ville',
        ),
        migrations.RemoveField(
            model_name='command',
            name='zip',
        ),
    ]
