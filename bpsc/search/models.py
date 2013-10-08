from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class HousingTag(Tag):
    pass


class CommunityTag(Tag):
    pass


class EmploymentTag(Tag):
    pass


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __uniocde__(self):
        return self.name

    class Meta:
        abstract = True


class HousingResource(Resource):
    tags = models.ManyToManyField(HousingTag, null=True, blank=True)
    posted = models.DateField()
    valid_until = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-valid_until']


class CommunityResource(Resource):
    tags = models.ManyToManyField(CommunityTag, null=True, blank=True)


class EmploymentResource(Resource):
    tags = models.ManyToManyField(EmploymentTag, null=True, blank=True)
    posted = models.DateField()

    class Meta:
        ordering = ['-posted']
