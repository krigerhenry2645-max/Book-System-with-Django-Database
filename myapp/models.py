from django.db import models

CATEGORIES = [
    ('Politics', 'Politics'),
    ('Story', 'Story'),
    ('Education', 'Education'),
]
#C:\Users\Administrator\PycharmProjects\DjangoDatabase\db.sqlite3

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORIES, max_length=100)
    isbn = models.CharField(unique=True, max_length=15,null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cost = models.IntegerField()
    year = models.IntegerField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title