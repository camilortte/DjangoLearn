from django.contrib import admin
from books.models import Editor , Autor, Libro

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class AdminBooks(admin.ModelAdmin):	
	list_display = ('title','publication_date')
	search_fields = ('title','publication_date')

admin.site.register(Editor)
admin.site.register(Autor, AuthorAdmin)
admin.site.register(Libro, AdminBooks)