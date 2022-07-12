from django.contrib import admin
from .models import clima
from import_export.admin import ImportExportActionModelAdmin

class ClimaAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(clima, ClimaAdmin)