# Generated by Django 4.1.5 on 2023-03-23 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_members_mentoremail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='Mentee',
            new_name='mentee',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='Mentor',
            new_name='mentor',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='Mentoremail',
            new_name='mentoremail',
        ),
        migrations.RenameField(
            model_name='members',
            old_name='Username',
            new_name='username',
        ),
    ]
