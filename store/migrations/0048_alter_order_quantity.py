# Generated by Django 4.2 on 2023-04-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
