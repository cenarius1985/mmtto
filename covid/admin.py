from django.contrib import admin
from .models import covid
from import_export.admin import ImportExportActionModelAdmin

class CovidAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(covid, CovidAdmin)