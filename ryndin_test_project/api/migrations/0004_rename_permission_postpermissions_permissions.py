# Generated by Django 5.1.3 on 2024-11-19 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_post_division_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postpermissions',
            old_name='permission',
            new_name='permissions',
        ),
    ]
