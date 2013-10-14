from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class HousingTag(Tag):
    #Category
    category = models.CharField(blank=True, max_length=50)
    housing_type = models.CharField(blank=True)
    county = models.CharField(blank=True)

    #Price
    price = models.IntegerField(blank=True)
    thirty_percent_ami = models.BooleanField(blank=True)
    
    
    #Occupancy
    sro = models.BooleanField(blank=True)
    studio = models.BooleanField(blank=True)
    one_br = models.BooleanField(blank=True)
    one_br_plus = models.BooleanField(blank=True)



class CommunityTag(Tag):
    #Types
    tabs = models.CharField(blank=True)


class EmploymentTag(Tag):
    pass

class LegalTag(Tag):
    pass


class Resource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    address = models.CharField(blank=True)
    city = models.CharField(blank=True)
    zipcode = models.IntegerField(blank=True)
    latitude = models.DecimalField(blank=True)
    longitude = models.DecimalField(balnk=True)
    phone = models.CharField(blank=True)

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


class LegalResource(Resource):
    tags = models.ManyToManyField(LegalTag, null=True, blank=True)
