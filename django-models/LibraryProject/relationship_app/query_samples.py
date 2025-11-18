import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # uses related_name='books'
    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title} by {book.author.name}")


# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarians = library.librarians.all()  # uses related_name='librarians'
    print(f"Librarians at {library_name}:")
    for librarian in librarians:
        print(f"- {librarian.name} ({librarian.email})")


# Sample executions (you can change names as needed)
if __name__ == "__main__":
    books_by_author("John Doe")
    print("\n")
    books_in_library("Central Library")
    print("\n")
    librarian_of_library("Central Library")
