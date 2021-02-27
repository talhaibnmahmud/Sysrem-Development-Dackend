from django.contrib import admin


class RentalBDAdminSite(admin.AdminSite):
    site_header = 'RentalBD Administration'
    site_title = 'RentalBD Admin'
    index_title = 'Model Administration'


admin_site = RentalBDAdminSite(name='RentalBD-Admin')

