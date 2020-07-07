from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, SiteUser


class SiteAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('is_active','is_staff', 'is_superuser', 'is_admin')
    fieldsets = (
        ('Login', {'fields': ('email', 'username', 'password')}),
        ('Personal', {'fields': ('first_name', 'last_name', 'date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin','is_superuser',)})
    )

admin.site.register(SiteUser, SiteAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')
    search_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)