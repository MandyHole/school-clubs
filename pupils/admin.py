from django.contrib import admin
from .models import Parent, Pupil, BookClub, Breakfast, BreakfastRequest, DateRequest

# Register your models here.
# admin.site.register(Breakfast)
# admin.site.register(Supper)
admin.site.register(Parent)
# admin.site.register(BookClub)
# admin.site.register(DateRequest)


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = (
        'first_name_of_pupil',
        'surname_of_pupil',
        'year_gp',
        'contact_email_for_pupil')
    list_filter = (
        'year_gp',
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
        'advance_year'
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


# @admin.register(BreakfastRequest)
# class BRequestAdmin(admin.ModelAdmin):
#     list_display = (
#         'additional_breakfast',
#         'cancel_breakfast',
#         'approved',
#         'request_date',
#         'pupil'
#         )
#     ordering = ['request_date']
#     actions = ['approve_request']

#     def approve_request(self, request, queryset):
#         queryset.update(approved=True)

@admin.register(DateRequest)
class DateRequestAdmin(admin.ModelAdmin):
    list_display = (
        'approval_status',
        'date_request',
        'type_of_request',
        'request_date',
        'pupil'
        )
    ordering = ['date_request']
    actions = ['approve_request', 'deny_lack_notice', 'deny_unavailable']

    def approve_request(self, request, queryset):
        queryset.update(approval_status=1)

    def deny_lack_notice(self, request, queryset):
        queryset.update(
            approval_status=2,
            why_declined=2
        )

    def deny_unavailable(self, request, queryset):
        queryset.update(
            approval_status=2,
            why_declined=1
        )