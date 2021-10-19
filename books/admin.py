from django.contrib import admin
from  .models import Book, Author

class BookInlineAdmin(admin.TabularInline):
    model = Book


class AutorAdmin(admin.ModelAdmin):
    inlines = [BookInlineAdmin]


admin.site.register(Author, AutorAdmin)
