from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MetaContent(models.Model):
    description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = (
            ('content_type', 'object_id'),
        )

    def __str__(self):
        return 'Meta'


@python_2_unicode_compatible
class URLMetaContent(models.Model):
    url = models.CharField('URL', max_length=200, unique=True)
    description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)

    class Meta:
        verbose_name = 'URL meta content'

    def __str__(self):
        return self.url
