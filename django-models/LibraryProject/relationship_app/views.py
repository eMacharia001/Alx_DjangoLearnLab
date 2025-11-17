from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/book_list.html', {'books': books})
