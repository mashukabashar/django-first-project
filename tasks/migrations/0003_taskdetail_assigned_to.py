# Generated by Django 5.1.6 on 2025-05-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_taskdetail_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskdetail',
            name='assigned_to',
            field=models.ManyToManyField(to='tasks.employee'),
        ),
    ]
