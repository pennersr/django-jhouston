from django.forms import ModelForm

from models import ErrorReport

class ErrorReportForm(ModelForm):
    
    class Meta:
        fields = ('message', 'url', 'line_number',)
        model = ErrorReport
