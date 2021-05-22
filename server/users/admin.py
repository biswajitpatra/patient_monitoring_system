from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Patient, Doctor

admin.site.register(Patient)
admin.site.register(Doctor)

class UserAdmin(BaseUserAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, UserAdmin)