# Generated by Django 4.0.6 on 2024-03-18 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo', models.TextField()),
                ('data_artigo', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('biografia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('data_comentario', models.DateTimeField(auto_now_add=True)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacaoArtigos.artigo')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacaoArtigos.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.IntegerField()),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacaoArtigos.artigo')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacaoArtigos.autor')),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AplicacaoArtigos.autor'),
        ),
    ]
