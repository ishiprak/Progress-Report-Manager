from django.shortcuts import render, redirect
from django import views
from .forms import ProgressForm
from .models import Progress

# Create your views here.
class FormView(views.View):
    def get(self, request):
        context = {
            "form" : ProgressForm(None)
        }
        return render(request, "progress_report.html", context=context)

    def post(self, request):
        if request.method=='POST':
            form = ProgressForm(request.POST)
            if form.is_valid:
                form.save()
            else:
                raise form.ValidationError("Form data not correctly filled!")
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
