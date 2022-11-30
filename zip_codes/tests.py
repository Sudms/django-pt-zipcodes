from datetime import datetime

import unittest

from  zip_codes.models import County, District, PostalCode 

class TestZipCodeMethods(unittest.TestCase):

    def test_district(self):
        district_code='01'
        district_name='Aveiro'

        district_create = District.objects.create(district_code=district_code, district_name=district_name)
        district_create.save()

        return district_create

    def test_county(self):
        district_code='01'
        county_code='16'
        county_name='Sao Joao da Madeira'

        county_create = County.objects.create(district_code=district_code,county_code=county_code, county_name=county_name)
        county_create.save()

        return county_create

    def test_zip_code(self):
        address_create = PostalCode.objects.create(
        district_name =  'Aveiro',
        county_name = 'Agueda',
        county_code = '1',
        district_code = '1',
        country_name =  'Portugal',
        locality_name = 'Póvoa do Vale do Trigo',
        locality_code = 'Alcafaz',
        artery_type = 'Beco',
        prep1 = 'das',
        artery_name = 'Flores', 
        postal_code = 3750,
        postal_code_extension = 364,
        postal_designation = 'BELAZAIMA DO CHÃO',
        created_on = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds'),
        updated_on = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
        )
        address_create.save()

        return address_create
