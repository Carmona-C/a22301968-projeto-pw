# Generated by Django 4.0.6 on 2024-05-02 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_banda_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Banda',
        ),
        migrations.DeleteModel(
            name='Musica',
        ),
    ]
