from django.contrib import admin

from Backend.admin import admin_site
from contact.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    search_fields = ('name', 'phone', 'email',)


admin_site.register(Contact, ContactAdmin)
admin.site.register(Contact, ContactAdmin)
