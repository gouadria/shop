# Generated by Django 4.2 on 2023-04-17 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_command_address_command_email_command_pays_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='date_command',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
