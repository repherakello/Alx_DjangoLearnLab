### Delete Operation
```python
book.delete()
Book.objects.all()  # Verify deletion
# Expected output: <QuerySet []> (no books in the database)
