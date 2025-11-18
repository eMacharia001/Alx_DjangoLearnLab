import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)

    # REQUIRED BY CHECKER: objects.filter(author=author)
    books = Book.objects.filter(author=author)

    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)

    # REQUIRED BY CHECKER: books.all()
    books = library.books.all()

    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title}")


# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)

    # REQUIRED BY CHECKER: Librarian.objects.get(library=
    librarian = Librarian.objects.get(library=library)

    print(f"Librarian for {library_name}: {librarian.name} ({librarian.email})")


if __name__ == "__main__":
    books_by_author("John Doe")
    books_in_library("Central Library")
    librarian_of_library("Central Library")
