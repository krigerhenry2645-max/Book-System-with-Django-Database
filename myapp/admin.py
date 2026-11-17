from django.contrib import admin

from myapp.models import Book

# Register your models here.
admin.site.site_title="HENKRITECH"
admin.site.site_header="HENKRITECH Bookshop Admin"
admin.site.index_title="Bookks Management System"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','year','price','category','isbn')
    search_fields = ('title','price','category','isbn')
    list_filter = ('category','year',)
    ordering = ('-year',)