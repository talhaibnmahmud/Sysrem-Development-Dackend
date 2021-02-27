from django.contrib import admin

from Backend.admin import admin_site
from rental.models import Division, District


# Register your models here.
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    empty_value_display = '--'


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'latitude', 'longitude',)
    list_filter = ('division',)
    empty_value_display = '--'


admin_site.register(Division, DivisionAdmin)
admin_site.register(District, DistrictAdmin)

admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
