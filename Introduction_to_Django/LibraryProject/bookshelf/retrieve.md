# retrieve operation
from bookshelf.models import Book

# Retrieve all books
book = Book.objects.get(title="1984")
book


#output
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

