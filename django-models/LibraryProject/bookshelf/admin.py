from django.contrib import admin
from .models import Book

# Customize the admin interface for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns visible in list view
    search_fields = ('title', 'author')                     # enable search
    list_filter = ('publication_year',)                     # add filter by year

# Register Book with the custom admin class
admin.site.register(Book, BookAdmin)
