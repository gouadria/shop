# Generated by Django 4.2 on 2023-04-09 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_alter_product_options_product_date_ajout_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nom',
            new_name='name',
        ),
    ]
