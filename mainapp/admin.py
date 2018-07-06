from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Contract


class UserAdmin(UserAdmin):

    fieldsets = [
        ('User Info', {
            'fields': ['username', 'password', 'user_type', ]
            }),
        ('Personal info', {
            'fields': [
                'first_name',
                'last_name',
                'phone',
                'email',
                'date_of_birth',
            ]
            }),
        ('Permissions', {
            'fields': ['is_active', 'is_staff', 'is_superuser',]
            }),
    ]

class ContractAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'organiser',
        'vendor',
        'date_of_contract',
        'price',
        'description',
        'contract_type',
    ]

    list_display_links = [
        'id',
    ]

    list_editable = [
        'vendor',
        'organiser',
        'date_of_contract',
        'price',
        'description',
        'contract_type',

    ]


admin.site.register(User, UserAdmin)
admin.site.register(Contract, ContractAdmin)
