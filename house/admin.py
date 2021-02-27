from django.contrib import admin

from Backend.admin import admin_site
from house.models import House


# Register your models here.
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'type', 'district', 'created',)
    list_filter = ('type', 'created', 'division',)
    search_fields = ['title', ]
    list_per_page = 25
    date_hierarchy = 'created'


admin_site.register(House, HouseAdmin)
admin.site.register(House, HouseAdmin)
