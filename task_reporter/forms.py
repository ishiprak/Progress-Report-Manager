from django import forms
from .models import (
    reports, 
    team_leads, 
    Progress
)

class DateType(forms.DateInput):
    input_type = "date"

class FileType(forms.FileInput):
    input_type = "file"

class ProgressForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': "form-control"}))
    reports = forms.ChoiceField(label='Reports', choices=reports, widget=forms.Select(attrs={'class': "form-control"}))
    no_of_hours = forms.IntegerField(label='No of Hours', widget=forms.NumberInput(attrs={'class': "form-control"}))
    today_progress = forms.CharField(label="TODAY'S PROGRESS", widget=forms.TextInput(attrs={'class': "form-control"}))
    concerns = forms.CharField(label='CONCERN IF ANY', widget=forms.Textarea(attrs={'rows' : 2, 'class': "form-control"}))
    next_plans = forms.CharField(label='NEXT PLAN', widget=forms.Textarea(attrs={'rows' : 2, 'class': "form-control"}))
    team_lead = forms.ChoiceField(label='Team Lead', choices=team_leads, widget=forms.RadioSelect(attrs={
        "style" : 'style="display: inline; list-style-type: none; margin-right: 10px;', "id" : "tech_lead"
    }))
    date = forms.DateField(label='DATE', widget=DateType(attrs={
        "placeholder" : "dd-mm-yy"
    }))
    class Meta:
        model = Progress
        fields = '__all__'

    # def save(self):
    #     if self.is_valid:
    #         self.save()
    #     else:
    #         raise forms.ValidationError("Please provide required inputs")

        