# Generated by Django 3.2.5 on 2022-03-29 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0069_rename_country_alumni_country_alumni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni',
            old_name='Country_alumni',
            new_name='Country',
        ),
    ]
