# Generated by Django 4.2 on 2023-04-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_remove_article_nbre_article_command_nbre_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
