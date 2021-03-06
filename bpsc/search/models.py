from django.db import models

from ckeditor.fields import RichTextField


class Tag(models.Model):
    tag_type = models.CharField('Tag Category', max_length=255,
            help_text='Category of this tag (e.g. Location, Price, etc.)')
    value = models.CharField('Tag Value', max_length=255, unique=True,
        help_text='Value of this tag (e.g. Berkeley, $400 Max, etc.)')

    def __unicode__(self):
        return self.tag_type + ': ' + self.value

    class Meta:
        abstract = True
        unique_together = ('tag_type', 'value')
        ordering = ['tag_type', 'value']


class HousingTag(Tag):
    class Meta(Tag.Meta):
        verbose_name = 'Housing Resource Tag'


class CommunityTag(Tag):
    class Meta(Tag.Meta):
        verbose_name = 'Community Resource Tag'


class EmploymentTag(Tag):
    class Meta(Tag.Meta):
        verbose_name = 'Employment Resource Tag'


class LegalTag(Tag):
    class Meta(Tag.Meta):
        verbose_name = 'Legal Resource Tag'


class Resource(models.Model):
    name = models.CharField('Name', max_length=255)
    description = RichTextField('Description',blank=True)
    url = models.URLField('URL', blank=True)
    street_address = models.CharField('Street Address', max_length=255, blank=True)
    city = models.CharField('City', max_length=255, blank=True)
    zipcode = models.IntegerField('ZIP Code', null=True, blank=True)
    latitude = models.DecimalField('Latitude', max_digits=8, decimal_places=5, null=True, blank=True)
    longitude = models.DecimalField('Longitude', max_digits=8, decimal_places=5, null=True, blank=True)
    phone = models.CharField('Phone', max_length=11, blank=True)
    num_used = models.IntegerField('Number of Uses', default=0,
            help_text='Number of times this resource has been given to a client')
    auto_added = models.BooleanField('Auto-added', default=False,
            help_text='Set to "true" if resource was automatically added')

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class HousingResource(Resource):
    posted = models.DateField('Date Posted', auto_now_add=True)
    outdated = models.BooleanField('Outdated', default=False,
            help_text='Set to "true" if it has been more than 6 weeks since this resource was posted')
    tags = models.ManyToManyField(HousingTag, verbose_name='Tags', null=True, blank=True)

    class Meta:
        ordering = ['auto_added', '-posted']
        verbose_name = 'Housing Resource'


class CommunityResource(Resource):
    posted = models.DateField('Date Posted', auto_now_add=True)
    tags = models.ManyToManyField(CommunityTag, verbose_name='Tags', null=True, blank=True)

    class Meta:
        ordering = ['auto_added']
        verbose_name = 'Community Resource'


class EmploymentResource(Resource):
    posted = models.DateField('Date Posted', auto_now_add=True)
    outdated = models.BooleanField('Outdated', default=False,
            help_text='Set to "true" if it has been more than 6 weeks since this resource was posted')
    listing_of_the_week = models.BooleanField('Listing of the Week', default=False,
            help_text='Set to "true" if this resource has been marked as a "Listing of the Week"')
    tags = models.ManyToManyField(EmploymentTag, verbose_name='Tags', null=True, blank=True)

    class Meta:
        ordering = ['auto_added', '-posted']
        verbose_name = 'Employment Resource'


class LegalResource(Resource):
    tags = models.ManyToManyField(LegalTag, verbose_name='Tags',null=True, blank=True)

    class Meta:
        ordering = ['auto_added']
        verbose_name = 'Legal Resource'

class BatchHousingResource(models.Model):
    prop = models.CharField('Property', max_length=2550)
    types_of_units = models.CharField('Types of Units', max_length=2550)
    amenities = models.CharField('Amenities', max_length=2550)
    income_requirements = models.CharField('Income Requirements', max_length=2550)
    rent_occupancy = models.CharField('Rent/Occupancy Limits', max_length=2550)
    how_to_apply = models.CharField('How to Apply', max_length=2550)
    posted = models.DateField('Posted', auto_now_add=True)
    outdated = models.BooleanField('Outdated', default=False)

    class Meta:
        verbose_name = 'Housing Resource (CSV)'
        verbose_name_plural = 'Housing Resources (CSV)'
