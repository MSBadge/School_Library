from django.contrib import admin
from books.models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'isbn', 'publication_date', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('genre', 'publication_date')
    ordering = ('-created_at',)