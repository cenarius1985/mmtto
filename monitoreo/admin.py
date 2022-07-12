from django.contrib import admin
from .models import monitoreo
from import_export.admin import ImportExportActionModelAdmin

class MonitoreoAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(monitoreo, MonitoreoAdmin)



   
   
    
    