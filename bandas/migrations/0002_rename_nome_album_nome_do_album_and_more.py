# Generated by Django 4.0.6 on 2024-04-18 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='nome',
            new_name='nome_do_album',
        ),
        migrations.RenameField(
            model_name='banda',
            old_name='nome',
            new_name='nome_da_banda',
        ),
        migrations.RenameField(
            model_name='musica',
            old_name='nome',
            new_name='nome_da_musica',
        ),
    ]
