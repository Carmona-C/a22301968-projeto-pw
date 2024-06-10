from bandas.models import *
import json

Banda.objects.all().delete()

with open('bandas/json/banda.json') as f:
    bandas = json.load(f)

    for banda in bandas:
        Banda.objects.create(
            nome_da_banda=banda['nome'],
            genero=banda['genero'],
            nacionalidade=banda['nacionalidade'],
            ano_criacao=banda['ano_criacao'],
            foto=banda['foto']
        )

Album.objects.all().delete()
Musica.objects.all().delete()


with open('bandas/json/discos.json') as f:
    discos = json.load(f)

    for disco in discos:
        banda, created = Banda.objects.get_or_create(nome_da_banda=disco['banda'])

        album = Album.objects.create(
            banda=banda,
            nome_do_album=disco['nome_album']
        )

        for musica_data in disco['musicas']:
            Musica.objects.create(
                album=album,
                nome_da_musica=musica_data['titulo'],
                duracao=musica_data['duracao'],  # Adicionando a duração da música
                spotify_link=''
            )


