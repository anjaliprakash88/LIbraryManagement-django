# Generated by Django 4.2.1 on 2023-08-23 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0006_alter_issueditem_issue_date_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
    ]
