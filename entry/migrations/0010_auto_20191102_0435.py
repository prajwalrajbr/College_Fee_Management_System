# Generated by Django 2.2.5 on 2019-11-02 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0009_auto_20191102_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='F_Type',
        ),
        migrations.AddField(
            model_name='stud_pd',
            name='Date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stud_pd',
            name='DOB',
            field=models.DateTimeField(),
        ),
    ]
