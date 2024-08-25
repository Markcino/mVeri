# Generated by Django 5.1 on 2024-08-25 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcriptrequest',
            name='doc_type',
            field=models.CharField(choices=[('None', 'None'), ('Degree', 'Degree'), ('diploma', 'Diploma'), ('certificate', 'Certificate'), ('transcript', 'Transcript'), ('recommendation_letter', 'Recommendation Letter')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='transcriptrequest',
            name='institution',
            field=models.ForeignKey(default=0.1, on_delete=django.db.models.deletion.CASCADE, to='accounts.administratorprofile'),
            preserve_default=False,
        ),
    ]
