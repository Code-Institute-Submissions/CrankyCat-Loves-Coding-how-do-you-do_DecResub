from django.contrib import admin
from .models import AddFeeling
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(AddFeeling)
class AddFeelingAdmin(SummernoteModelAdmin):
    
    list_display = (
        'date',
        'feelings',
        'details',
    )

    summernote_fields = ('details')
