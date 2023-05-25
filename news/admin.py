from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import News


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = "__all__"
