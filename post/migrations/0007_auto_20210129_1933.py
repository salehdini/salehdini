# Generated by Django 3.1.5 on 2021-01-29 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='crerated_date',
            new_name='created_date',
        ),
    ]