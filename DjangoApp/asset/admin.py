from django.contrib import admin
from .models import Employee, Company, Asset, Device, DelegateDevice


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_companies')
    list_filter = ('companies',)

    def get_companies(self, obj):
        return ", ".join([str(company) for company in obj.companies.all()])

    get_companies.short_description = 'Companies'


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('employees',)


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'asset_type', 'company', 'employee','checked_in_at', 'checked_out_at', )
    list_filter = ('company', 'employee')


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'condition', 'asset','checked_in_at', 'checked_out_at',)


class DelegateDeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset', 'device', 'employee', 'delegation_date',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DelegateDevice, DelegateDeviceAdmin)
