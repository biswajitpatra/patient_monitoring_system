from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Patient, Doctor

class PatientAdmin(admin.ModelAdmin):
    filter_horizontal = ('doctors',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor)

class UserAdmin(BaseUserAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)