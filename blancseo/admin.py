from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import MetaContent, URLMetaContent


class MetaContentInlineAdmin(GenericStackedInline):
    model = MetaContent
    max_num = 1


@admin.register(URLMetaContent)
class URLMetaContentAdmin(admin.ModelAdmin):
    search_fields = ('url',)
