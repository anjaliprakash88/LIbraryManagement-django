# Generated by Django 4.2.3 on 2023-07-30 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_remove_book_book_add_date_remove_book_book_add_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
    ]