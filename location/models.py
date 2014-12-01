from django.db import models
from django.utils.translation import ugettext_lazy as _


CONTINENTS = (
    ('AF', _('Africa')),
    ('NA', _('North America')),
    ('EU',  _('Europe')),
    ('AS', _('Asia')),
    ('OC',  _('Oceania')),
    ('SA', _('South America')),
    ('AN', _('Antarctica'))
)


class Country(models.Model):
    """
    International Organization for Standardization (ISO) 3166-1 Country list    
    """
    iso2_code = models.CharField(_('ISO alpha-2'), max_length=2, null=True, blank=True)
    name = models.CharField(_('Official name (CAPS)'), max_length=128)
    printable_name = models.CharField(_('Country name'), max_length=128)
    iso3_code = models.CharField(_('ISO alpha-3'), max_length=3, null=True, blank=True)
    numcode = models.CharField(_('ISO numeric'),max_length=100, null=True, blank=True)
    fips_104 = models.CharField(_('FIPS 10-4'), max_length=100, null=True, blank=True)
    internet = models.CharField(_('Intenet'), max_length=100, null=True, blank=True)
    capital = models.CharField(_('Capital'), max_length=100, null=True, blank=True)
    map_reference = models.CharField(_('Map Reference'), max_length=100, null=True, blank=True)
    nationality_singular = models.CharField(_('Nationality Singular'), max_length=100, null=True, blank=True)
    nationality_plural = models.CharField(_('Nationality Plural'), max_length=100, null=True, blank=True)
    currency = models.CharField(_('Currency'), max_length=100, null=True, blank=True)
    currency_code = models.CharField(_('Currency code'), max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('name',)

    def __unicode__(self):
        return self.printable_name


class State(models.Model):
    """
    Administrative division for a country. State is a generic name, for some countries this 
    is equivalent to Province/Region/Territories/Departments
    """
    country = models.ForeignKey(Country)
    name = models.CharField(_('State/Province name'), max_length=60)
    abbr = models.CharField(_('State/Province Abbreviation'), max_length=10, null=True, blank=True)
    adm1_code = models.CharField(_('State/Province ADM1 code'), max_length=60, null=True, blank=True)
    
    class Meta:
        verbose_name = _('State/Province')
        verbose_name_plural = _('States/Provinces')
        ordering= ('name',)

    def __unicode__(self):
        return self.name

class City(models.Model):
    """
    Administrative division for a country. State is a generic name, for some countries this 
    is equivalent to Province/Region/Territories/Departments
    """
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    name = models.CharField(_('City/Location name'), max_length=60)
    abbr = models.CharField(_('City/Location Abbreviation'), max_length=10, null=True, blank=True)
    latitude = models.CharField(_('City/Location latitude'), max_length=60, null=True, blank=True)
    longitude = models.CharField(_('City/Location longitude'), max_length=60, null=True, blank=True)
    timezone = models.CharField(_('City/Location timezone'), max_length=60, null=True, blank=True)
    
    class Meta:
        verbose_name = _('City/Location')
        verbose_name_plural = _('Cities/Locations')
        ordering= ('name',)

    def __unicode__(self):
        return self.name