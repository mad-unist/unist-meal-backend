# from django.contrib import admin

# from .models import Rating

# # Register your models here.
# admin.site.register(Rating)

from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Rating

class RatingAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Rating, RatingAdmin)