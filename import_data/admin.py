from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import MyData

@admin.register(MyData)
class MyDataAdmin(ImportExportModelAdmin):
    list_display = ('busy_po_no','party_name','product_name','qty_main')