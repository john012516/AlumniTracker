# Generated by Django 3.2.5 on 2022-03-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITAT', '0064_merge_20220325_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='employed',
            name='Company_country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='Course',
            field=models.CharField(choices=[('BSIT', 'BSIT'), ('BSCS', 'BSCS')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employed',
            name='Income',
            field=models.CharField(choices=[('10,000-20,000', '10,000-20,000'), ('20,000-30,000', '20,000-30,000'), ('30,000-40,000', '30,000-40,000'), ('50,000-70,000', '40,000-50,000'), ('70,000-80,000', '70,000-80,000'), ('80,000-90,000', '80,000-90,000'), ('90,000-100,000', '90,000-100,000')], max_length=200, null=True),
        ),
    ]
