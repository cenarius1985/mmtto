from django.contrib import admin
from .models import rrhh
from import_export.admin import ImportExportActionModelAdmin

class RrhhAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(rrhh, RrhhAdmin)