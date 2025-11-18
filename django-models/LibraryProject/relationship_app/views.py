from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Author, Book

# Function-Based View
def list_all_books(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return render(request, "relationship_app/list_books.html", {"books_text": output})

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# User Registration View

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # create new user
            login(request, user)    # auto login after registration
            return redirect("list_books")  # redirect wherever you want
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})
