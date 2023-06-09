# Generated by Django 4.2 on 2023-04-19 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_alter_command_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date_Article', models.DateTimeField(blank=True, null=True)),
                ('quantite', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='Articles',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.article'),
            preserve_default=False,
        ),
    ]
