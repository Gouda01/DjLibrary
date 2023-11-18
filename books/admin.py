from django.contrib import admin
from .models import Book , Author , Review


class ProductAdmin (admin.ModelAdmin):
    list_display = ['title','price']
    list_filter = ['price','publication_date']
    search_fields = ['title','author']



# Register your models here.
admin.site.register(Book,ProductAdmin)
admin.site.register(Author)
admin.site.register(Review)



