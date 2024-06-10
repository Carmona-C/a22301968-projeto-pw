import requests
from django.shortcuts import render
from datetime import datetime

def previsao_lisboa(request):
    # Endpoint da API do IPMA para a previsão do tempo
    previsao_url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"
    tipo_tempo_url = "https://api.ipma.pt/open-data/weather-type-classe.json"

    # Obter dados da previsão
    previsao_response = requests.get(previsao_url)
    previsao_data = previsao_response.json()  # Garantir que estamos lidando com um dicionário

    # Obter dados dos tipos de tempo
    tipo_tempo_response = requests.get(tipo_tempo_url)
    tipo_tempo_data = tipo_tempo_response.json()  # Garantir que estamos lidando com um dicionário

    hoje_previsao = previsao_data['data'][0]

    nome_cidade = "Lisboa"
    temp_min = hoje_previsao['tMin']
    temp_max = hoje_previsao['tMax']
    data_previsao = datetime.strptime(hoje_previsao['forecastDate'], "%Y-%m-%d").strftime("%d/%m/%Y")
    id_weather_type = hoje_previsao['idWeatherType']

    # Obter a descrição do tempo
    descricao_tempo = next(item['descWeatherTypePT'] for item in tipo_tempo_data['data'] if item['idWeatherType'] == id_weather_type)

    icone_animated = f'meteo/w_ic_d_{id_weather_type:02d}anim.svg'

    context = {
        'nome_cidade': nome_cidade,
        'temp_min': temp_min,
        'temp_max': temp_max,
        'data_previsao': data_previsao,
        'descricao_tempo': descricao_tempo,
        'icone_animated': icone_animated,
    }

    return render(request, 'meteo/previsao_lisboa.html', context)




def previsao_tempo(request):
    previsao_url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"
    tipo_tempo_url = "https://api.ipma.pt/open-data/weather-type-classe.json"

    # Obter dados da previsão
    previsao_response = requests.get(previsao_url)
    previsao_data = previsao_response.json()

    # Obter dados dos tipos de tempo
    tipo_tempo_response = requests.get(tipo_tempo_url)
    tipo_tempo_data = tipo_tempo_response.json()

    previsao = previsao_data['data']

    lista = []

    dic_dias = {
        "Monday": "Segunda-Feira",
        "Tuesday": "Terça-Feira",
        "Wednesday": "Quarta-Feira",
        "Thursday": "Quinta-Feira",
        "Friday": "Sexta-Feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"}


    for hoje in previsao:
        descricao_tempo = next(item['descWeatherTypePT'] for item in tipo_tempo_data['data'] if item['idWeatherType'] == hoje['idWeatherType'])
        icone_animated = f'meteo/w_ic_d_{hoje["idWeatherType"]:02d}anim.svg'
        nome_cidade = "Torres Vedras"
        temp_min = hoje['tMin']
        temp_max = hoje['tMax']
        data_previsao = datetime.strptime(hoje['forecastDate'], "%Y-%m-%d").strftime("%d/%m/%Y")
        dia_semana = datetime.strptime(hoje['forecastDate'], "%Y-%m-%d").strftime("%A")



        informacao = {
            'temp_min': temp_min,
            'temp_max': temp_max,
            'data_previsao': data_previsao,
            'dia_semana': dic_dias[dia_semana],
            'descricao_tempo': descricao_tempo,
            'icone_animated': icone_animated,
            'nome_cidade': nome_cidade,
        }
        lista.append(informacao)

    return render(request, 'meteo/previsao_tempo.html', {'previsoes': lista})


