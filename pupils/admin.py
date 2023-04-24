from django.contrib import admin
from admin_totals.admin import ModelAdminTotals
from .models import Pupil, DateRequest
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce

# Register your models here.


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = (
        'booking_approval_status',
        'first_name_of_pupil',
        'surname_of_pupil',
        'year_gp',
        'contact_email_for_pupil')
    list_filter = (
        'year_gp',
        'booking_approval_status',
        'b_mon',
        'b_tues',
        'b_wed',
        'b_thurs',
        'b_fri',
        's_mon',
        's_tues',
        's_wed',
        's_thurs',
        's_fri'
        )
    actions = [
        'advance_year',
        'approve_booking',
        'add_breakfast_fee',
        'add_supper_fee',
        'reset_billing_cycle'
    ]
    ordering = ['surname_of_pupil']

    def advance_year(self, request, queryset):
        Pupil.objects.filter(year_gp='6').delete()
        Pupil.objects.filter(year_gp='5').update(year_gp='6')
        Pupil.objects.filter(year_gp='4').update(year_gp='5')
        Pupil.objects.filter(year_gp='3').update(year_gp='4')
        Pupil.objects.filter(year_gp='2').update(year_gp='3')
        Pupil.objects.filter(year_gp='1').update(year_gp='2')
        Pupil.objects.filter(year_gp='0').update(year_gp='1')

    def approve_booking(self, request, queryset):
        queryset.update(booking_approval_status=1)

    def reset_billing_cycle(self, request, queryset):
        queryset.update(amount_owed=0)


@admin.register(DateRequest)
class DateRequestAdmin(admin.ModelAdmin):
    list_display = (
        'approval_status',
        'date_request',
        'type_of_request',
        'request_date',
        'cost',
        'pupil'
        )
    list_totals = [
        ('cost', lambda field: Coalesce(Sum(field), 0)),
        ('cost', Avg)]
    ordering = ['date_request']
    actions = [
        'approve_add_breakfast',
        'approve_add_supper',
        'approve_cancel_breakfast',
        'approve_cancel_supper',
        'deny_lack_notice',
        'deny_unavailable',
        'calculate_amount_owed']
    list_filter = (
        'approval_status',
        'pupil'
    )

    def approve_add_breakfast(self, request, queryset):
        queryset.update(approval_status=1)
        queryset.update(cost='2')

    def approve_add_supper(self, request, queryset):
        queryset.update(approval_status=1)
        queryset.update(cost='2.50')

    def approve_cancel_breakfast(self, request, queryset):
        queryset.update(approval_status=1)
        queryset.update(cost='-2')

    def approve_cancel_supper(self, request, queryset):
        queryset.update(approval_status=1)
        queryset.update(cost='-2.50')

    def deny_lack_notice(self, request, queryset):
        queryset.update(
            approval_status=3,
        )
        queryset.update(cost='0')

    def deny_unavailable(self, request, queryset):
        queryset.update(approval_status=2)
        queryset.update(cost='0')

