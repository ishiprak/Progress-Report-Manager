import os
from django.shortcuts import render, redirect
from django import views, forms
from .forms import ProgressForm
from .models import Progress
from django.conf import settings
from django.http import HttpResponse, Http404


# Create your views here.
class FormView(views.View):
    def get(self, request):
        context = {
            "form" : ProgressForm(None)
        }
        return render(request, "progress_report.html", context=context)

    def post(self, request):
        if request.method=='POST':
            form = ProgressForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                raise forms.ValidationError("Form data not correctly filled!")
        return redirect("table")


class TableView(views.View):
    def get(self, request):
        ctx = {}
        progress_list = Progress.objects.all()
        ctx['header'] = ['#', 'Name', 'Date', 
                        'Reports', 'Team Lead', 'No of Hours', 
                        "Today's Progress", "Today's Document", 'Concerns', 
                        "Next Plans", 'Next Plans Document']
        ctx['rows'] = progress_list
        return render(request, "table.html", context=ctx)
    
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
