from django.contrib import admin
from collage.models import Notice
from django.contrib.admin.options import ModelAdmin

class NoticeAdmin(ModelAdmin):
    list_display =  ['subject','cr_date']
    search_fields = ['subject','cr_date']
    list_filter =   ['cr_date']


admin.site.register(Notice,NoticeAdmin)

# Register your models here.
