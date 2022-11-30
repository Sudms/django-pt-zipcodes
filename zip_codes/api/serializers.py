from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import Household
from zip_codes.models import PostalCode


class PostalCodeSerializer(ModelSerializer):
    postal_code = serializers.CharField(required=True)
    street_name = serializers.CharField(required=True)

    def to_representation(self, instance):
        zip_code = instance["zip_code"]
        zip_code_extension = instance["zip_code_extension"]
        qs_postal = PostalCode.objects.filter(
            postal_code=zip_code, postal_code_extension=zip_code_extension
        )
        response = {"streets": []}
        full_address = []
        if qs_postal:
            for i, item in enumerate(qs_postal):
                full_add = [
                    item.artery_type,
                    item.prep1,
                    item.artery_title,
                    item.prep2,
                    item.artery_name,
                    item.artery_local,
                ]
                full_name = " ".join(
                    each for each in full_add if not each.__eq__("nan")
                )
                full_address.append(full_name + ", " + item.district_name)
        return response

    class Meta:
        model = PostalCode
        fields = ("postal_code", "street_name")
