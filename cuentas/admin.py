from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta

# Register your models here.


class Account_Admin(UserAdmin):
    list_display= ('email', 'nombre', 'apellido', 'username', 'ultimo_acceso', 'is_active')
    list_display_links = ('email','nombre','apellido')
    readonly_fields = ('fecha_registro','ultimo_acceso')
    ordering = ('fecha_registro',)

    filter_horizontal=()
    list_filter =()
    fieldsets =()

admin.site.register(Cuenta, Account_Admin)