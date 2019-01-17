from __future__ import unicode_literals
from django.contrib.auth.admin import UserAdmin as UA
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import User, Store, Company


class UserAdmin(UA):

    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)

        abstract_fields = [field.name for field in AbstractUser._meta.fields]
        user_fields = [field.name for field in self.model._meta.fields]

        self.fieldsets += (
            (_('Extra fields'), {
                'fields': [
                    f for f in user_fields if (
                        f not in abstract_fields and
                        f != self.model._meta.pk.name
                    )
                ],
            }),
        )


class StoreOwnershipInline(admin.TabularInline):
    model = Store.owner.through


class StoreAdmin(admin.ModelAdmin):
    inlines = [StoreOwnershipInline, ]


class CompanyOwnershipInline(admin.TabularInline):
    model = Company.owner.through


class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyOwnershipInline, ]


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Store, StoreAdmin)
