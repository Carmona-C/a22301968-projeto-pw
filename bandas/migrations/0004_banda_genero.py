# Generated by Django 4.0.6 on 2024-04-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0003_remove_banda_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='genero',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
