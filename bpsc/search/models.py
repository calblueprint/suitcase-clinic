from django.db import models


class Tag(models.Model):
    tag_type = models.CharField(max_length=255)
    value = models.CharField(max_length=255, unique=True)

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
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    street_address = models.CharField(blank=True)
    city = models.CharField(blank=True)
    zipcode = models.IntegerField(blank=True)
    latitude = models.DecimalField(null=True, blank=True)
    longitude = models.DecimalField(null=True, blank=True)
    phone = models.CharField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class HousingResource(Resource):
    tags = models.ManyToManyField(HousingTag, null=True, blank=True)
    posted = models.DateField()
    valid_until = models.DateField(null=True, blank=True)
    outdated = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ['-valid_until']


class CommunityResource(Resource):
    tags = models.ManyToManyField(CommunityTag, null=True, blank=True)


class EmploymentResource(Resource):
    tags = models.ManyToManyField(EmploymentTag, null=True, blank=True)
    posted = models.DateField()
    valid_until = models.DateField(null=True, blank=True)
    outdated = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ['-posted']


class LegalResource(Resource):
    tags = models.ManyToManyField(LegalTag, null=True, blank=True)
