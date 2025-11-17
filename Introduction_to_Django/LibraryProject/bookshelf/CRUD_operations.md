# CRUD _operations
# Create Operation - Book Model

**Command:**

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
Book.objects.all()

>>> from bookshelf.models import Book
>>> 
>>> # Retrieve all books
>>> books = Book.objects.all()
>>> books
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
>>> 

