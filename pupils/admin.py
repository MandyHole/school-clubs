from django.contrib import admin
from .models import Parent, Pupil, BookClub, Breakfast

# Register your models here.
admin.site.register(Pupil)
admin.site.register(Breakfast)
# admin.site.register(Supper)
admin.site.register(Parent)
admin.site.register(BookClub)
