from urllib.request import urlretrieve, urlcleanup
import pandas as pd

from django.core.management.base import BaseCommand
from django.db import transaction

from zip_codes.models import  District, PostalCode, County

csv_link_codes = 'https://github.com/centraldedados/codigos_postais' \
                    '/raw/master/data/codigos_postais.csv'

csv_link_county = 'https://github.com/centraldedados/codigos_postais' \
                    '/raw/master/data/concelhos.csv'

csv_link_district = 'https://github.com/centraldedados/codigos_postais' \
                    '/raw/master/data/distritos.csv'


csv_file_dist = pd.read_csv(csv_link_district)
csv_file_county = pd.read_csv(csv_link_county)
csv_file_codes = pd.read_csv(csv_link_codes)

def search_district_codes(district_code):
    for i,row in csv_file_dist.reset_index().iterrows():
        if row['cod_distrito'] == district_code:
            return (row['nome_distrito'])

def search_county_codes(county_code):
    for i,row in csv_file_county.reset_index().iterrows():
        if row['cod_concelho'] == county_code:
            return (row['nome_concelho'])

class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args, **options):
        District.objects.all().delete()
        for i,row in csv_file_dist.reset_index().iterrows():
            District.objects.create(district_code=row['cod_distrito'], district_name=row['nome_distrito'])

        County.objects.all().delete()
        for i,row in csv_file_county.reset_index().iterrows():
            County.objects.create(district_code=row['cod_distrito'], county_code=row['cod_concelho'], county_name=row['nome_concelho'])

        PostalCode.objects.all().delete()
        for i,row in csv_file_codes.reset_index().iterrows():
            PostalCode.objects.create(
                country_name='Portugal',
                district_name=search_district_codes(row['cod_distrito']),
                county_name=search_county_codes(row['cod_concelho']),
                district_code=row['cod_distrito'],
                county_code=row['cod_concelho'], 
                locality_name=row['nome_localidade'],
                locality_code=row['cod_localidade'],
                artery_type=row['tipo_arteria'],
                prep1=row['prep1'],
                artery_title=row['titulo_arteria'],
                prep2=row['prep2'],
                artery_name=row['nome_arteria'],
                artery_local=row['local_arteria'],
                postal_code=row['num_cod_postal'],
                postal_code_extension=row['ext_cod_postal'],
                postal_designation=row['desig_postal'],
            )

