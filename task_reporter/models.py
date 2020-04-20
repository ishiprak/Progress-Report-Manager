from django.db import models
from datetime import datetime

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)

reports = [
        ("d", "DAILY"),
        ("w", "WEEKLY"),
        ("m", "MONTHLY")
    ]
team_leads = [
        ("Raktima Mitra", "Raktima Mitra"),
        ("Akansha", "Akansha"),
        ("Amitesh Ranjan", "Amitesh Ranjan"),
        ("Sheetal", "Sheetal"),
        ("Kanika", "Kanika"),
        ("Ajeet", "Ajeet"),
        ("Shekhar", "Shekhar")
    ]

class Progress(models.Model):
    name = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now_add=False)
    reports = models.CharField(max_length=50, choices=reports, blank=False)
    team_lead = models.TextField(blank=False, choices=team_leads)
    no_of_hours = models.IntegerField(blank=False)
    today_progress = models.CharField(max_length=50, blank=False)
    today_document = models.FileField(upload_to=user_directory_path)
    concerns = models.TextField()
    next_plans = models.TextField()
    next_plans_document = models.FileField(upload_to=user_directory_path) 
