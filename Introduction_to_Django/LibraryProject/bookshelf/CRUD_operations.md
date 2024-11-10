### Create Operation
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Output the created book
# Expected output: <Book: 1984 by George Orwell (1949)>


### Retrieve Operation
```python
book = Book.objects.get(id=1)
book
# Expected output: <Book: 1984 by George Orwell (1949)>


### Update Operation
```python
book.title = "Nineteen Eighty-Four"
book.save()
book
# Expected output: <Book: Nineteen Eighty-Four by George Orwell (1949)>



### Delete Operation
```python
book.delete()
Book.objects.all()  # Verify deletion
# Expected output: <QuerySet []> (no books in the database)
