# coding=utf-8
import time
import requests

from django.core.management.base import BaseCommand

from shiptrader import models as shiptrader_models


class Command(BaseCommand):
    help = 'Convert starships from https://swapi.co/documentation#starships to listings'

    provider = 'https://swapi.co/api/starships/'

    def filter_numerical(self, value):
        if isinstance(value, str):
            if ',' in value:
                return float(value.replace(',', '.'))
            if value == 'unknown':
                return 0
        return value

    def fetch_objects(self, provider=provider):
        self.stdout.write(self.style.SUCCESS(f'Fetching page {provider}...'))
        response = requests.get(provider).json()
        buffer = []
        for starship in response['results']:
            buffer.append(shiptrader_models.Listing(
                name=starship['name'],
                ship_type=shiptrader_models.Starship.objects.filter(starship_class=starship['starship_class']).first(),
                price=self.filter_numerical(starship['cost_in_credits'])
            ))

        shiptrader_models.Listing.objects.bulk_create(buffer)
        self.stdout.write(self.style.SUCCESS(f'\t>> Fetched {len(buffer)} starships.'))
        if response['next']:
            return self.fetch_objects(response['next'])

    def handle(self, **options):
        start_time = time.time()
        try:
            self.fetch_objects()
        except Exception as e:
            raise e
        finally:
            self.stdout.write(self.style.SUCCESS(
                '\n\nFinished in %.2f seconds.' % (time.time() - start_time)
            ))
