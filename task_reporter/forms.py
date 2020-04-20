from django import forms
from .models import Progress

class ProgressForm(forms.ModelForm):
    team_lead = forms.ChoiceField(choices=Progress.team_leads, widget=forms.RadioSelect(attrs={
        "style" : 'style="display: inline-block; margin-right: 10px;'
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        "placeholder" : "dd-mm-yy"
    }))
    class Meta:
        model = Progress
        fields = '__all__'
        