from django.contrib import admin

from myapp.models import ExcelData


class ExcelDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExcelData, ExcelDataAdmin)
