from django.contrib import admin
from lib_db.models import Book, Reader, Order, BooktableLogs, Genre, Publishing

# Register your models here.
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Order)
admin.site.register(Genre)
admin.site.register(Publishing)
admin.site.register(BooktableLogs)
