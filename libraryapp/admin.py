from django.contrib import admin
from .models import Book, IssuedItem, Author, Login


admin.site.register(Book)
admin.site.register(IssuedItem)
admin.site.register(Author)
admin.site.register(Login)
