# Generated by Django 3.1.5 on 2021-01-26 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210126_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
    ]
