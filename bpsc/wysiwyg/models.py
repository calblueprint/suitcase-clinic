from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField()
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50, unique=True)
    # content_basic = RichTextField('Basic', config_name='basic')
    # content_full = RichTextField('Full', config_name='full')
    # content_custom = RichTextField(config_name='custom', verbose_name='Custom')

    def __unicode__(self):
    	return "%(name)s at url: %(url)s " %\
		{"name": self.name, "url": self.url}
