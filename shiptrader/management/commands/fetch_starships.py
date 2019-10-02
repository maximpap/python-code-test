# coding=utf-8
import time
import requests

from django.core.management.base import BaseCommand

from shiptrader import models as shiptrader_models


class Command(BaseCommand):
    help = 'Fetch all starships from https://swapi.co/documentation#starships'

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
            buffer.append(shiptrader_models.Starship(
                starship_class=starship['starship_class'],
                manufacturer=starship['manufacturer'],
                length=self.filter_numerical(starship['length']),
                hyperdrive_rating=self.filter_numerical(starship['hyperdrive_rating']),
                cargo_capacity=self.filter_numerical(starship['cargo_capacity']),
                crew=self.filter_numerical(starship['crew']),
                passengers=self.filter_numerical(starship['passengers']),
            ))

        shiptrader_models.Starship.objects.bulk_create(buffer)
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
