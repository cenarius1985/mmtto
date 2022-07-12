from django.contrib import admin
from .models import licitacion
from import_export.admin import ImportExportActionModelAdmin

class LicitacionAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(licitacion, LicitacionAdmin)
