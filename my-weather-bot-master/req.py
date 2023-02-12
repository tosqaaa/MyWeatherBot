import json
import requests
import datetime
from keys import *


def req():
    with open('coord.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for item in data['coord']:
            lat = item['lat']
            lon = item['lon']

    future_weather_params = {"lat": f"{lat}", "lon": f"{lon}", "appid": API_KEY_OW,
                             "units": "metric", "cnt": f"{9}", "lang": 'ru'}
    current_weather_params = {"lat": f"{lat}", "lon": f"{lon}", "appid": API_KEY_OW,
                              "units": "metric", "lang": 'ru'}
    with open("coord.json", "w", encoding='utf-8') as f:
        pass

    response = requests.get(
        FUTURE_WEATHER_LINK,
        params=future_weather_params, headers=HEADERS)
    response_now = requests.get(
        CURRENT_WEATHER_LINK,
        params=current_weather_params, headers=HEADERS)

    arr = {'main': {},
           'now': {},
           'd1': {},
           'd2': {}
           }
    if response.status_code:
        arr['main']['status'] = 'true'
        arr['main']['country'] = response.json()['city']['country']
        arr['main']['city'] = response_now.json()['name']
        arr['main']['rise'] = datetime.datetime.fromtimestamp(
            int(response_now.json()['sys']['sunrise']+10800)).strftime('%d-%m-%Y %H:%M')
        arr['main']['set'] = datetime.datetime.fromtimestamp(
            int(response_now.json()['sys']['sunset']+10800)).strftime('%d-%m-%Y %H:%M')

        arr['now']['weather'] = response_now.json()['weather'][0]['description']
        arr['now']['temp'] = response_now.json()['main']['temp']
        arr['now']['humidity'] = response_now.json()['main']['humidity']
        arr['now']['wind'] = response_now.json()['wind']['speed']

        arr['d1']['time'] = datetime.datetime.fromtimestamp(
            int(response.json()['list'][1]['dt']+10800)
        ).strftime('%d-%m-%Y %H:%M')
        arr['d1']['weather'] = response.json(
        )['list'][1]['weather'][0]['description']
        arr['d1']['temp'] = response.json()['list'][1]['main']['temp']
        arr['d1']['humidity'] = response.json()['list'][1]['main']['humidity']
        arr['d1']['wind'] = response.json()['list'][1]['wind']['speed']

        arr['d2']['time'] = datetime.datetime.fromtimestamp(
            int(response.json()['list'][8]['dt']+10800)
        ).strftime('%d-%m-%Y %H:%M')
        arr['d2']['weather'] = response.json(
        )['list'][8]['weather'][0]['description']
        arr['d2']['temp'] = response.json()['list'][8]['main']['temp']
        arr['d2']['humidity'] = response.json()['list'][8]['main']['humidity']
        arr['d2']['wind'] = response.json()['list'][8]['wind']['speed']

        with open('resp_to_print.json', 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=4, ensure_ascii=False)
