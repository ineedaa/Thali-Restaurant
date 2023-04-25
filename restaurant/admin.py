from django.contrib import admin
from .models import Booking,Comment
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Booking)
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    summernote_fields = ('post')