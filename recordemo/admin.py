from django.contrib import admin
from .models import AddFeeling
from django_summernote.admin import SummernoteModelAdmin


# this decorator will register both our post model and
# the post admin class with our admin site
@admin.register(AddFeeling)
class AddFeelingAdmin(SummernoteModelAdmin):
    
    list_display = (
        'user_profile',
        'date',
        'feelings',
        'details',
    )

    summernote_fields = ('details')
