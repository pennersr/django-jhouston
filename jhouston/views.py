from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from forms import ErrorReportForm

@csrf_exempt
def onerror(request):
    if request.method != 'POST':
        ret = HttpResponse(content="Sorry, we accept POST only", status=400)
    else:
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.remote_addr = request.META['REMOTE_ADDR']
            report.user_agent = request.META['HTTP_USER_AGENT']
            report.save()
            ret = HttpResponse(content='Thanks for reporting', 
                               status=201)
        else:
            ret = HttpResponse(content=form._errors, status=400)
    return ret

