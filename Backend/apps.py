from django.contrib.admin.apps import AdminConfig


class RentalBDAdminConfig(AdminConfig):
    default_site = 'Backend.admin.RentalBDAdminSite'
