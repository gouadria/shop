# Generated by Django 4.2 on 2023-04-16 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='orders',
        ),
        migrations.AddField(
            model_name='cart',
            name='orders',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.order'),
            preserve_default=False,
        ),
    ]
