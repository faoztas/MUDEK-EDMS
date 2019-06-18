# Django
from django.contrib import admin

# Local Django
from core.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = (
        'first_name', 'last_name', 'email',
        'message', ('create_date', 'update_date')
    )
    readonly_fields = ('create_date', 'update_date')

    list_display = ('first_name', 'last_name', 'email', 'admin_read')
    list_filter = ('create_date', 'update_date')
    search_fields = ('first_name', 'last_name', 'email')

    def get_fields(self, request, *args, **kwargs):
        fields = super(ContactAdmin, self).get_fields(request, *args, **kwargs)
        exclude_fields = []

        if 'add' in request.path.split('/'):
            exclude_fields += [('create_date', 'update_date')]

        return [field for field in fields if field not in exclude_fields]
