from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-Based View
def list_all_books(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return render(request, "relationship_app/book_list.html", {"books_text": output})

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
