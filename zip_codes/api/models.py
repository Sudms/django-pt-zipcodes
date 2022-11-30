from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
#model for District(distritos.csv from ctt)
class District(models.Model):
    district_code = models.CharField(max_length=10, verbose_name=_("District code"), db_index=True)
    district =  models.CharField(max_length=255, verbose_name=_("District"))

#model for County(concelhos.csv from ctt)
class County(models.Model):
    district_code = models.CharField(max_length=10, verbose_name=_("District code"))
    county_code = models.CharField(max_length=10, verbose_name=_("County code"), db_index=True)
    county = models.CharField(max_length=255, verbose_name=_("County"))

#model for PostalCode(códigos_postais.csv from ctt)
class PostalCode(models.Model):
    district = models.CharField(max_length=255, verbose_name=_('District'),blank=True, null=True)
    county = models.CharField(max_length=255, verbose_name=_('County'), blank=True, null=True)

    county_code = models.CharField(max_length=10, verbose_name=_("County code"), db_index=True)
    district_code = models.CharField(max_length=10, verbose_name=_("District code"), db_index=True)
    country = models.CharField(max_length=20, verbose_name=_("Country"), blank=True, null=False)
    locality = models.CharField(max_length=125, verbose_name=_("Locality"),blank=True, null=False)
    locality_code = models.CharField(max_length=10, verbose_name=_("Locality code"),blank=True, null=False)

    artery_type = models.CharField(max_length=255, blank=True, null=True)
    prep1 = models.CharField(max_length=255, blank=True, null=True)
    artery_title = models.CharField(max_length=255, blank=True, null=True)
    prep2 = models.CharField(max_length=255, blank=True, null=True)
    artery_name = models.CharField(max_length=255, blank=True, null=True)
    artery_local = models.CharField(max_length=255, blank=True, null=True)

    postal_code = models.IntegerField(verbose_name=_("Postal Code"), help_text='cp4', blank=False, null=False, db_index=True)
    postal_code_extension = models.IntegerField(verbose_name=_("Postal Code Extension"), help_text='cp3', blank=False, null=False, db_index=True)
    postal_designation = models.CharField(max_length=255, verbose_name=_("Postal Designation"), blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Postal Code')
        verbose_name_plural = _('Postal Codes')
