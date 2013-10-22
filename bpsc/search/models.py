from django.db import models


class Tag(models.Model):
    tag_type = models.TextField(max_length=255)
    value = models.TextField(max_length=255, unique=True)

    def __unicode__(self):
        return self.tag_type + ': ' + self.value

    class Meta:
        abstract = True
        unique_together = ('tag_type', 'value')


class HousingTag(Tag):
    pass


class CommunityTag(Tag):
    pass


class EmploymentTag(Tag):
    pass


class LegalTag(Tag):
    pass


class Resource(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    street_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    phone = models.CharField(max_length=11, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class HousingResource(Resource):
    tags = models.ManyToManyField(HousingTag, null=True, blank=True)
    posted = models.DateField()
    expires = models.BooleanField(blank=True)
    outdated = models.BooleanField(blank=True)
    rent = models.IntegerField(blank=True)

    class Meta:
        ordering = ['-posted']


class CommunityResource(Resource):
    tags = models.ManyToManyField(CommunityTag, null=True, blank=True)
    cost = models.IntegerField(blank=True)
    insurance = models.BooleanField(blank=True)


class EmploymentResource(Resource):
    tags = models.ManyToManyField(EmploymentTag, null=True, blank=True)
    posted = models.DateField()
    expires = models.BooleanField(blank=True)
    outdated = models.BooleanField(blank=True)

    class Meta:
        ordering = ['-posted']


class LegalResource(Resource):
    tags = models.ManyToManyField(LegalTag, null=True, blank=True)
