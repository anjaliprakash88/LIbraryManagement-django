# Generated by Django 4.2.3 on 2023-07-30 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_add_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_add_time',
        ),
    ]
