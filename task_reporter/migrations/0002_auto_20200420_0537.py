# Generated by Django 3.0.5 on 2020-04-20 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_reporter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='next_plan',
            new_name='next_plans',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='next_plan_doc',
            new_name='next_plans_document',
        ),
        migrations.RenameField(
            model_name='progress',
            old_name='today_doc',
            new_name='today_document',
        ),
    ]
