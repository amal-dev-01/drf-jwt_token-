# Generated by Django 4.2.6 on 2023-10-22 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('token_jwt', '0002_student_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
