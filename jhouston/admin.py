from django.contrib import admin

from models import ErrorReport

class ErrorReportAdmin(admin.ModelAdmin):
    search_fields = ('message',
                     'url',
                     'user_agent',
                     'data')
    date_hierarchy = 'reported_at'
    list_display = ('reported_at', 
                    'message', 
                    'url', 
                    'line_number',
                    'user_agent',
                    'remote_addr')

admin.site.register(ErrorReport, ErrorReportAdmin)
