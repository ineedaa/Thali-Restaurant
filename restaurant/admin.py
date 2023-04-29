from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display =('name','number_of_guests','date','time')
    search_fields=('name','email','date')

