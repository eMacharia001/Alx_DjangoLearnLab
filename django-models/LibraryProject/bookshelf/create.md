from bookshelf.models import Book

# create a book instance 
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
Book.objects.all()

# output
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

