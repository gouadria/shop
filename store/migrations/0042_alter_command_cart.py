# Generated by Django 4.2 on 2023-04-19 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_alter_article_quantite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='Cart',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.cart'),
        ),
    ]
