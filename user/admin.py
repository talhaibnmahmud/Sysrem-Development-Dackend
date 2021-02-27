from django.contrib import admin

from Backend.admin import admin_site
from user.models import Customer


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)
    search_fields = ('name', 'email', 'phone',)
    exclude = ('user',)


admin_site.register(Customer, CustomerAdmin)
admin.site.register(Customer, CustomerAdmin)
