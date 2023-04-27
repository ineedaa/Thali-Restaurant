from django.contrib import admin
from .models import Booking,Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display =('name','number_of_guests','date','time','updated_on')
    search_fields=('name','email','date')

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('post')