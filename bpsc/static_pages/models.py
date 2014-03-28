from django.db import models

from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse_lazy


class Post(models.Model):
    content = RichTextField()
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
    	return "%(name)s at url: %(url)s " % {"name": self.name, "url": reverse_lazy(self.url)}

    class Meta:
        db_table = 'wysiwyg_post'
