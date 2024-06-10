# Generated by Django 4.0.6 on 2024-04-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacaoCurso', '0005_remove_projeto_github_link_remove_projeto_imagem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='github_link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(default='default_imagem.jpg', upload_to='projeto_imagens'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='video_demo_link',
            field=models.URLField(default=''),
        ),
    ]
