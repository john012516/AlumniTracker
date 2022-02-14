# Generated by Django 3.1.7 on 2022-01-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0007_remove_joinevent_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinevent',
            name='lastname',
        ),
        migrations.AddField(
            model_name='joinevent',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
