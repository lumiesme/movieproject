from urllib.request import urlopen
import os
import django
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movieproject.settings')
django.setup()
from movieapp.models import Movie

url = 'https://restcountries.com/v3.1/all'

response = urlopen(url)
data = json.loads(response.read())
counter = 0
my_data = []

for country in data:
    current = {}

    if 'capital' in country:
        current['common'] = country['name']['common']
        current['official'] = country['name']['official']
        current['capital'] = country['capital'][0]
        current['region'] = country['region']
        if "subregion" in country:
            current['subregion'] = country['subregion']
        else:
            current['subregion'] = None

        current['flag'] = country['flags']['png']
        current['map'] = country['maps']['googleMaps']

        my_data.append(current)
        counter += 1

Country.objects.all().delete()

for cur in my_data:
    common = cur['common']
    official = cur['official']
    capital = cur['capital']
    region = cur['region']
    subregion = cur['subregion']
    flag = cur['flag']
    maps = cur['map']
    Country.objects.create(common=common, official=official, capital=capital, region=region, subregion=subregion,
                           flag=flag, map=maps)

print(f'Total {counter} countries.')