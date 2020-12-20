from django.contrib import admin
from .models import Members
from import_export.admin import ImportExportModelAdmin
from main.resources import MemberResource


# @admin.register(Members)
class MembersAdmin(ImportExportModelAdmin):
    list_display = ['member_id', 'Full_name', 'Shop_Name',
                    'Principal_Activity', 'Operation_Mode', 'Dues_Payment']
    search_fields = ['member_id', 'Full_name']
    list_filter = ['Date_registered', 'Gender', 'Dues_Payment']
    list_per_page = 50
    actions = ('change_payment_negative', 'change_payment_positive')
    date_hierarchy = 'Date_registered'
    resource_class = MemberResource

    def change_payment_negative(self, request, queryset):
        count = queryset.update(Dues_Payment='UnPaid')
        self.message_user(request, '{} Dues changed to UnPaid'.format(count))
    change_payment_negative.short_description = 'Unpay Dues'

    def change_payment_positive(self, request, queryset):
        count = queryset.update(Dues_Payment='Paid')
        self.message_user(request, '{} Dues changed to Paid'.format(count))
    change_payment_positive.short_description = 'Pay Dues'


admin.site.register(Members, MembersAdmin)
