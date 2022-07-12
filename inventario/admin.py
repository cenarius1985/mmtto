from django.contrib import admin
from .models import inventario
from import_export.admin import ImportExportActionModelAdmin

class InventarioAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(inventario, InventarioAdmin)