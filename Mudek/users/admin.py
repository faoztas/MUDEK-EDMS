# Django
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.auth.admin import UserAdmin as _UserAdmin

# Local
from users.models import User, ActivationKey, ResetPasswordKey


@admin.register(User)
class UserAdmin(_UserAdmin):
    fieldsets = (
        (_('Base'), {
            'fields': ('email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_verified', 'is_academician',
                'is_department_manager', 'is_assistant_department_manager',
                'is_dean_manager', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
        (_('Important dates'), {
            'fields': ('last_login',)
        }),
    )
    readonly_fields = ('last_login',)

    add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': (
               'email', 'first_name', 'last_name',
               'password1', 'password2'
           )
       }),
    )

    list_display = (
        'first_name', 'last_name', 'email',
        'is_active', 'is_verified', 'is_superuser', 'is_academician',
        'is_department_manager', 'is_assistant_department_manager',
        'is_dean_manager'
    )
    list_filter = (
        'is_active', 'is_verified', 'is_superuser', 'is_academician',
        'is_department_manager', 'is_assistant_department_manager',
        'is_dean_manager'
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name')


@admin.register(ActivationKey)
class ActivationKeyAdmin(admin.ModelAdmin):
    fields = ('key', 'user', 'is_used')
    readonly_fields = ('key', 'user', 'is_used')

    list_display = ('user', 'key', 'is_used')
    list_filter = ('is_used',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

    def has_add_permission(self, request):
        return False


@admin.register(ResetPasswordKey)
class ResetPasswordKeyAdmin(admin.ModelAdmin):
    fields = ('key', 'user', 'is_used')
    readonly_fields = ('key', 'user', 'is_used')

    list_display = ('user', 'key', 'is_used')
    list_filter = ('is_used',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

    def has_add_permission(self, request):
        return False
