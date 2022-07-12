from django.contrib import admin
from .models import industriales
from import_export.admin import ImportExportActionModelAdmin

class IndustrialesAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(industriales, IndustrialesAdmin)