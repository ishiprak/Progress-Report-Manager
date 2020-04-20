from django.shortcuts import render
from django import views
from .forms import ProgressForm

# Create your views here.
class FormView(views.View):
    def get(self, request):
        context = {
            "form" : ProgressForm
        }
        return render(request, "progress_report.html", context=context)
